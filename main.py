from Stock_list import prices

class Stock:
    
    def __init__(self,name,price,quantity):
        self.stock_name = name
        self.stock_price = price
        self.stock_quantity = quantity
    
    def calculate(self):
        return self.stock_price * self.stock_quantity
    
    def __str__(self):
        return f"{self.stock_name} | Qty: {self.stock_quantity} | Value: {self.calculate()}"

class Portfolio():
    def __init__(self):
        self.stocks = []

    def add_stock(self, new_stock):

        for stock in self.stocks:

            if stock.stock_name == new_stock.stock_name:
                stock.stock_quantity += new_stock.stock_quantity
                return

        self.stocks.append(new_stock)
    
    def total_investment(self):
        total = 0
        for stock in self.stocks:
            total += stock.calculate()
        return total
    
    def show_portfolio(self):
        print("\nPortfolio Summary")
        print("-" * 30)

        for stock in self.stocks:
            print(
                f"{stock.stock_name} | "
                f"Qty: {stock.stock_quantity} | "
                f"Value: ${stock.calculate()}"
                )
    
    def save_to_file(self):
        with open("portfolio.txt", "w") as file:
            for stock in self.stocks:
                file.write(f"Stock: {stock.stock_name}\n")
                file.write(f"Price: {stock.stock_price}\n")
                file.write(f"Quantity: {stock.stock_quantity}\n")
                file.write(f"Value: {stock.calculate()}\n\n")
            file.write(f"Total Investment: {self.total_investment()}")
        print("Portfolio saved successfully!")

def main():
    portfolio = Portfolio()
    
    print("\nAvailable Stocks:")
    print(", ".join(prices.keys()))

    while True:
        name = input("Enter stock name: ").upper()

        if name not in prices:
            print("Stock not available")
            continue

        price = prices[name]

        try:
            quantity = int(input("Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if not portfolio.stocks:
            print("Portfolio is empty.")
            return

        stock = Stock(name, price, quantity)
        portfolio.add_stock(stock)
        
        choice = input("Add another stock? (y/n): ")

        if choice.lower() == "n":
            break
    
    if not portfolio.stocks:
        print("Portfolio is empty.")
        return

    portfolio.show_portfolio()
    print("Total Investment:", portfolio.total_investment())
    portfolio.save_to_file()


if __name__ == "__main__":
    main()