def get_valid_input():
    stock = input("Enter stock quantity (or type quit): ")

    if stock == "quit":
        return "quit"

    elif stock.startswith("-") and stock[1:].isdigit():
            print("Error: Stock quantity cannot be negative.")
            return None

    elif not stock.isdigit():
            print("Error: Please enter a valid number.")
            return None
    else:
         return int(stock)
    

while True:
    stock = input("Enter stock quantity (or type quit): ")

    if stock == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", rejected_entries)
        break

    elif stock.startswith("-") and stock[1:].isdigit():
        print("Error: Stock quantity cannot be negative.")
        rejected_entries += 1
        continue

    elif not stock.isdigit():
        print("Error: Please enter a valid number.")
        rejected_entries += 1
        continue

    else:
        stock = int(stock)
        inventory += stock

        print("Current inventory: ", inventory)

        if inventory > 500:
            print("Alert: Inventory exceeds 500 units!")
            break