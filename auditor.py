inventory = 0
print(inventory)

while True:
    stock = input("Enter stock quantity (or type quit): ")

    if stock == "quit":
        break

    if not stock.isdigit():
        print("Error: Please enter a valid number.")
        continue

    stock = int(stock)
    print(stock)