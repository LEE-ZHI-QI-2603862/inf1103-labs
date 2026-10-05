import json
import os

def load_inventory():
    if os.path.exists("inventory.json"):
         print("inventory.json found.")
    
         with open("inventory.json", "r") as f:
            inventory = json.load(f)

         print("Inventory loaded successfully.")
         return inventory

    else:
         print("inventory.json not found. Starting with empty inventory.")
         return []

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

def display_all():
     print("Current Inventory")
     print("--------------------------------------------")

     for product in inventory:
          print(
               f"ID: {product['id']} | "
               f"Name: {product['name']} | "
               f"Price: {product['price']:.2f} | "
               f"Stock: {product['stock']}"
          )
     print("--------------------------------------------")

def add_product():
     print("Add New Product")

     product_id = input("Product ID: ")
     name = input("Product Name: ")
     price = float(input("Price: "))
     stock = int(input("Stock Quantity: "))

     product = {
          "id": product_id,
          "name": name,
          "price": price,
          "stock": stock 
     }

     inventory.append(product)

     print("Product added successfully!")

def search_product():
     print("Search Product")

     product_id = input("Enter Product ID: ")

     for product in inventory:
          if product["id"] == product_id:
               print("Product Found")
               print("--------------------------------------------")
               print("ID:", product["id"])
               print("Name:", product["name"])
               print(f"Price: ${product['price']:.2f}")
               print("Stock:", product["stock"])
               print("--------------------------------------------")
               return
     print("Product not found.")

def update_stock():
     print("Update Stock")

     product_id = input("Enter Product ID: ")

     for product in inventory:
          if product["id"] == product_id:
               print("Product Found:")
               print("Name:", product["name"])
               print("Current Stock:", product["stock"])

               new_stock = int(input("New Stock Quantity: "))

               product["stock"] = new_stock

               print("Stock updated successfully!")
               return
     
     print("Product not found.")

inventory = load_inventory()

load_inventory()