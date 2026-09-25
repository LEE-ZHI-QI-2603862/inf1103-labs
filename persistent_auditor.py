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

inventory = 0
rejected_entries = 0
deliveries_processed = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        generate_report(inventory,rejected_entries)
        print("Total Deliveries Processed:", deliveries_processed)
        break

    elif stock is None:
        rejected_entries += 1
        continue

    else:
        inventory = process_delivery(inventory, stock)
        deliveries_processed += 1

        tax = calculate_tax(stock)

        print("Tax for this delivery:", tax)
        print("Current inventory: ", inventory)

        if inventory > 500:
            print("Alert: Inventory exceeds 500 units!")
            break