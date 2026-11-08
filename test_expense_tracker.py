"""Unit tests. Run with:  python -m unittest test_expense_tracker -v"""
import io
import unittest
from contextlib import redirect_stdout
from decimal import Decimal
from unittest.mock import patch

import expense_tracker as core
import expense_tracker_bonus as bonus


class TestGatekeeper(unittest.TestCase):
    def test_string_to_number(self):
        self.assertEqual(core.parse_amount("100"), 100.0)
        self.assertEqual(core.parse_amount("  12.50 "), 12.5)

    def test_string_concatenation_disaster_avoided(self):
        # '100' + '50' would be '10050' as strings; as numbers it is 150
        self.assertEqual(core.parse_amount("100") + core.parse_amount("50"), 150.0)

    def test_rejects_invalid_input(self):
        for bad in ["ten", "", "   ", "-5", "0", "nan", "inf", "1,5x"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    core.parse_amount(bad)


class TestAccumulator(unittest.TestCase):
    def test_add_expense(self):
        self.assertEqual(core.add_expense(100, 50), 150)

    def test_format_money(self):
        self.assertEqual(core.format_money(150), "$150.00")
        self.assertEqual(core.format_money(1234.5), "$1,234.50")


class TestMainLoop(unittest.TestCase):
    def run_main(self, inputs):
        buffer = io.StringIO()
        with patch("builtins.input", side_effect=inputs), redirect_stdout(buffer):
            core.main()
        return buffer.getvalue()

    def test_handles_five_plus_transactions(self):
        out = self.run_main(["100", "50", "20", "10", "5", "15", "quit"])
        self.assertIn("Transactions recorded: 6", out)
        self.assertIn("TOTAL SPENT: $200.00", out)

    def test_invalid_input_does_not_crash_or_change_total(self):
        out = self.run_main(["100", "ten", "-5", "", "50", "quit"])
        self.assertIn("Invalid data", out)
        self.assertIn("TOTAL SPENT: $150.00", out)

    def test_quit_is_case_insensitive_and_trimmed(self):
        out = self.run_main(["20", "  QUIT  "])
        self.assertIn("TOTAL SPENT: $20.00", out)

    def test_quit_immediately(self):
        out = self.run_main(["quit"])
        self.assertIn("No expenses recorded.", out)
        self.assertIn("TOTAL SPENT: $0.00", out)

    def test_closed_input_still_prints_total(self):
        out = self.run_main(["30", EOFError()])
        self.assertIn("TOTAL SPENT: $30.00", out)


class TestBonus(unittest.TestCase):
    def test_decimal_precision(self):
        a, b = bonus.parse_amount("0.10"), bonus.parse_amount("0.20")
        self.assertEqual(a + b, Decimal("0.30"))          # floats would give 0.30000000000000004

    def test_rounds_to_cents(self):
        self.assertEqual(bonus.parse_amount("2.345"), Decimal("2.35"))

    def test_rejects_invalid(self):
        for bad in ["ten", "", "-1", "0", "NaN", "Infinity"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    bonus.parse_amount(bad)

    def test_totals_and_undo(self):
        items = []
        bonus.add_expense(items, Decimal("100.00"), "food")
        bonus.add_expense(items, Decimal("50.00"), "Travel")
        bonus.add_expense(items, Decimal("20.00"), " food ")
        self.assertEqual(bonus.total_of(items), Decimal("170.00"))
        self.assertEqual(bonus.category_totals(items)["Food"], Decimal("120.00"))
        bonus.undo_last(items)
        self.assertEqual(bonus.total_of(items), Decimal("150.00"))
        self.assertIsNone(bonus.undo_last([]))


if __name__ == "__main__":
    unittest.main()
