class Product:
    def __init__(self, product_id, name, cost_price, selling_price):
        self.product_id = product_id
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def view_products(self):
        for product_id, product in self.products.items():
            print(f"Product ID: {product_id}")
            print(f"Name: {product.name}")
            print(f"Cost Price: R{product.cost_price:,.2f}")
            print(f"Selling Price: R{product.selling_price:,.2f}")
            print()

class Sales:
    def __init__(self):
        self.sales = []

    def make_sale(self, product_id, quantity):
        if product_id not in inventory.products:
            print("Product not found.")
            return

        product = inventory.products[product_id]
        line_total = product.selling_price * quantity
        sale = {
            "product_id": product_id,
            "quantity": quantity,
            "line_total": line_total,
        }
        self.sales.append(sale)
        print(f"Sale recorded: Total Amount R{line_total:,.2f}")

class Reporting:
    def __init__(self):
        pass

    def generate_report(self, sales):
        total_sales = sum(sale['line_total'] for sale in sales)
        total_cost = sum(
            inventory.products[sale['product_id']].cost_price * sale['quantity']
            for sale in sales
        )
        total_profit = total_sales - total_cost

        print("------- Sales Report -------")
        print(f"Total Number of Sales: {len(sales)}")
        print(f"Total Sales: R{total_sales:,.2f}")
        print(f"Total Cost: R{total_cost:,.2f}")
        print(f"Total Profit: R{total_profit:,.2f}")

# Initialize the system
inventory = Inventory()
sales_system = Sales()
reporting_system = Reporting()

while True:
    print("\n---- Point-of-Sale Menu ----")
    print("1. Add Product")
    print("2. View Products")
    print("3. Make a Sale")
    print("4. Generate Report")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        cost_price = float(input("Enter Cost Price: "))
        selling_price = float(input("Enter Selling Price: "))
        
        product = Product(product_id, name, cost_price, selling_price)
        inventory.add_product(product)
        print("Product added successfully.")
    
    elif choice == "2":
        inventory.view_products()
    
    elif choice == "3":
        product_id = input("Enter Product ID: ")
        quantity = float(input("Enter Quantity: "))
        sales_system.make_sale(product_id, quantity)
    
    elif choice == "4":
        reporting_system.generate_report(sales_system.sales)
    
    elif choice == "5":
        break

print("Exiting the Point-of-Sale system.")
