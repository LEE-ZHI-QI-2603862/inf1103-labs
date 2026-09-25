def load_inventory():
    try:
        with open("inventory.txt", "r") as f:
            lines = f.readlines()

            if len(lines) >= 1 and lines[0].strip() != "":
                saved_total = int(lines[0].strip())
            else:
                saved_total = 0

            if len(lines) >= 2 and lines[1].strip() != "":
                saved_history = [int(x) for x in lines[1].strip().split(",")]
            else:
                saved_history = []

            print("Previous inventory loaded successfully.")
            return saved_total, saved_history

    except FileNotFoundError:
        print("No previous inventory file found. Starting fresh.")
        return 0, []

def save_inventory(total, history):
    with open("inventory.txt", "w") as f:
        f.write(str(total) + "\n")
        f.write(",".join(str(x) for x in history) + "\n")

    print("Inventory successfully saved to inventory.txt")

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

def process_delivery(current_total, new_value):
     new_total = current_total + new_value
     return new_total

def calculate_tax(amount):
     tax = amount * 0.10
     return tax

def generate_report(total_units, failed_attempts):
     print("Total Units Processed:", total_units)
     print("Number of Failed/Rejected Entries", failed_attempts)


inventory, history = load_inventory()
rejected_entries = 0
deliveries_processed = 0

print("Current Inventory Total:", inventory)
print("Previous Transaction History:", history)

while True:
    stock = get_valid_input()

    if stock == "quit":
        generate_report(inventory,rejected_entries)
        print("Total Deliveries Processed:", deliveries_processed)
        save_inventory(inventory, history)
        break

    elif stock is None:
        rejected_entries += 1
        continue

    else:
        inventory = process_delivery(inventory, stock)
        deliveries_processed += 1
        history.append(stock)

        tax = calculate_tax(stock)

        print("Tax for this delivery:", tax)
        print("Current inventory: ", inventory)
        print("Transaction history so far:", history)

        if inventory > 500:
            print("Alert: Inventory exceeds 500 units!")
            break