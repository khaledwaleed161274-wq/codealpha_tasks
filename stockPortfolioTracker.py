# ============================================================
# CodeAlpha - Task 2: Stock Portfolio Tracker
# ============================================================

import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190,
}


def show_available_stocks():
    print("Available stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def ask_quantity():
    while True:
        text = input("Enter quantity: ").strip()

        try:
            quantity = int(text)
        except ValueError:
            print("Error: quantity must be a whole number (e.g. 5).\n")
            continue

        if quantity <= 0:
            print("Error: quantity must be greater than zero.\n")
            continue

        return quantity


def collect_portfolio():
    portfolio = {}

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"Error: '{symbol}' is not in the available stocks.\n")
            continue

        quantity = ask_quantity()

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} x {symbol}.\n")

    return portfolio


def build_report(portfolio):
    lines = []
    lines.append("=== Portfolio Summary ===")
    lines.append(f"{'Stock':<8}{'Price':>10}{'Quantity':>10}{'Value':>12}")
    lines.append("-" * 40)

    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        lines.append(f"{symbol:<8}{price:>10}{quantity:>10}{value:>12}")

    lines.append("-" * 40)
    lines.append(f"Total Investment Value: ${total}")
    return lines, total


def save_report(portfolio, report_lines, total):
    choice = input("Save report to a file? (txt / csv / no): ").strip().lower()

    if choice == "no" or choice == "":
        print("Report not saved.")
        return

    try:
        if choice == "txt":
            with open("portfolio_report.txt", "w", encoding="utf-8") as file:
                file.write("\n".join(report_lines) + "\n")
            print("Saved to portfolio_report.txt")

        elif choice == "csv":
            with open("portfolio_report.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Stock", "Price", "Quantity", "Value"])
                for symbol, quantity in portfolio.items():
                    price = STOCK_PRICES[symbol]
                    writer.writerow([symbol, price, quantity, price * quantity])
                writer.writerow(["Total Investment Value", "", "", total])
            print("Saved to portfolio_report.csv")

        else:
            print("Invalid choice. Report not saved.")

    except OSError:
        print("Error: could not write the file.")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    show_available_stocks()

    portfolio = collect_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    print()
    report_lines, total = build_report(portfolio)
    for line in report_lines:
        print(line)
    print()

    save_report(portfolio, report_lines, total)


if __name__ == "__main__":
    main()