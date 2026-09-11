inventory = 0
print(inventory)

while True:
    stock = input("Enter stock quantity (or type quit): ")

    if stock == "quit":
        break

    if not stock.isdigit():
        print("Error: Please enter a valid number.")
        continue

    if stock.startswith("-") and stock[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        continue

    stock = int(stock)

    inventory += stock

    print("Current inventory: ", inventory)