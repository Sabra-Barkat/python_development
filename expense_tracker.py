"""
Project 2: The Expense Tracker
DecodeLabs - Python Programming (Math operations & Accumulators)

IPO model:
    Input   -> the user types an expense amount (a raw string)
    Process -> the gatekeeper converts it to a number, the accumulator adds it
    Output  -> the Total Spent is displayed
"""
import math


def parse_amount(text):
    """GATEKEEPER: convert raw text into a positive number.

    Raises ValueError for anything invalid ("ten", "", "-5", "0", "nan", "inf").
    """
    amount = float(text.strip())                 # "100" -> 100.0 (raises ValueError for "ten")
    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be a positive number")
    return amount


def add_expense(total, amount):
    """MODEL: the accumulator pattern -> State(new) = State(old) + Input."""
    return total + amount


def format_money(value):
    """VIEW helper: format a number as money, e.g. 1234.5 -> $1,234.50"""
    return f"${value:,.2f}"


def main():
    total = 0.0          # STATE: initialized OUTSIDE the loop so it is never reset
    count = 0            # how many valid expenses were recorded

    print("=" * 34)
    print("   Welcome to the Expense Tracker!")
    print("=" * 34)
    print("Enter each expense amount (e.g. 100, 50, 20.50).")
    print("Type 'quit' when you are done.\n")

    try:
        while True:                                          # the continuous audit loop
            raw = input(f"Expense #{count + 1} amount (or 'quit'): ").strip().lower()

            if raw == "quit":                                # KILL SWITCH (sentinel value)
                break

            try:                                             # DEFENSIVE CODING (poka-yoke)
                amount = parse_amount(raw)
            except ValueError:
                print("  Invalid data. Please enter a positive number like 25 or 12.50.")
                continue                                     # skip the bad input, keep the total safe

            total = add_expense(total, amount)               # ACCUMULATE: total += new_expense
            count += 1
            print(f"  Added {format_money(amount)} | Running total: {format_money(total)}")
    except (EOFError, KeyboardInterrupt):
        print()                                              # Ctrl+C / closed input: still show the total

    # OUTPUT: final result
    print("\n" + "=" * 34)
    if count == 0:
        print("No expenses recorded.")
    else:
        print(f"Transactions recorded: {count}")
    print(f"TOTAL SPENT: {format_money(total)}")
    print("=" * 34)


if __name__ == "__main__":
    main()
