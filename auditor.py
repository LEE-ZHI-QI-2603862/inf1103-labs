inventory = 0
print(inventory)

while True:
    stock = input("Enter stock quantity (or type quit): ")

    if stock == "quit":
        break

    elif stock.startswith("-") and stock[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        continue

    elif not stock.isdigit():
        print("Error: Please enter a valid number.")
        continue

    else:
        stock = int(stock)
        inventory += stock

        print("Current inventory: ", inventory)

        if inventory > 500:
            print("Alert: Inventory exceeds 500 units!")
            break