"""
Project 2 (Bonus): Expense Tracker Pro

Extras beyond the core project:
  * Decimal arithmetic -> exact money math (no floating-point surprises)
  * Categories and a spending summary (count, average, highest, per category)
  * 'undo' and 'list' commands
  * Expenses are saved to expenses.json, so they survive a restart
"""
import json
import os
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")
CENT = Decimal("0.01")


# ---------- MODEL (data logic) ----------
def parse_amount(text):
    """GATEKEEPER: text -> positive Decimal rounded to cents, or ValueError."""
    try:
        amount = Decimal(text.strip())
        if not amount.is_finite() or amount <= 0:
            raise ValueError("Amount must be positive")
        return amount.quantize(CENT, rounding=ROUND_HALF_UP)
    except InvalidOperation:
        raise ValueError("Not a valid number")


def add_expense(expenses, amount, category):
    category = category.strip().title() or "General"
    expenses.append({"amount": amount, "category": category})


def undo_last(expenses):
    return expenses.pop() if expenses else None


def total_of(expenses):
    total = Decimal("0.00")                 # accumulator initialized OUTSIDE the loop
    for item in expenses:
        total += item["amount"]
    return total


def category_totals(expenses):
    totals = {}
    for item in expenses:
        totals[item["category"]] = totals.get(item["category"], Decimal("0.00")) + item["amount"]
    return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))


def load_expenses():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            raw = json.load(file)
        return [{"amount": Decimal(r["amount"]), "category": r["category"]} for r in raw]
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError, InvalidOperation):
        return []


def save_expenses(expenses):
    raw = [{"amount": str(e["amount"]), "category": e["category"]} for e in expenses]
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(raw, file, indent=2)


# ---------- VIEW (user interface) ----------
def money(value):
    return f"${value:,.2f}"


def show_list(expenses):
    print("\n------ Expenses ------")
    if not expenses:
        print("No expenses yet.")
    for number, item in enumerate(expenses, start=1):
        print(f"{number:>2}. {money(item['amount']):>12}  {item['category']}")
    print("----------------------")


def show_summary(expenses):
    print("\n" + "=" * 34)
    if not expenses:
        print("No expenses recorded.")
    else:
        total = total_of(expenses)
        average = (total / len(expenses)).quantize(CENT, rounding=ROUND_HALF_UP)
        highest = max(expenses, key=lambda e: e["amount"])
        print(f"Transactions : {len(expenses)}")
        print(f"Average      : {money(average)}")
        print(f"Highest      : {money(highest['amount'])} ({highest['category']})")
        print("By category  :")
        for name, value in category_totals(expenses).items():
            print(f"   {name:<12} {money(value):>12}")
    print(f"TOTAL SPENT  : {money(total_of(expenses))}")
    print("=" * 34)


def main():
    expenses = load_expenses()
    print("=" * 34)
    print("   Expense Tracker - Pro Edition")
    print("=" * 34)
    print(f"Loaded {len(expenses)} saved expense(s).")
    print("Enter an amount, or type: list / undo / quit\n")

    try:
        while True:
            raw = input("Amount or command: ").strip().lower()

            if raw == "quit":
                break
            if raw == "list":
                show_list(expenses)
                continue
            if raw == "undo":
                removed = undo_last(expenses)
                if removed:
                    save_expenses(expenses)
                    print(f"  Removed {money(removed['amount'])} ({removed['category']}).")
                else:
                    print("  Nothing to undo.")
                continue

            try:
                amount = parse_amount(raw)
            except ValueError:
                print("  Invalid data. Enter a positive number, or list / undo / quit.")
                continue

            category = input("  Category (press Enter for General): ")
            add_expense(expenses, amount, category)
            save_expenses(expenses)
            print(f"  Added {money(amount)} | Running total: {money(total_of(expenses))}")
    except (EOFError, KeyboardInterrupt):
        print()

    show_summary(expenses)


if __name__ == "__main__":
    main()
