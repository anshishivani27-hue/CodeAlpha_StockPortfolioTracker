stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

print("📈 Stock Portfolio Tracker")
print("--------------------------")

stock_name = input("Enter stock name (AAPL/TSLA/GOOGL): ").upper()

quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    total_value = stock_prices[stock_name] * quantity

    print("\nStock:", stock_name)
    print("Price per Share: $", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value: $", total_value)

else:
    print("❌ Stock not found!")
    