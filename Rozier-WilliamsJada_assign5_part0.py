number_of_prices = int(input("How many prices would you like to collect? "))
while number_of_prices <  0:
        print("Must be positive, try again")
        number_of_prices = True
      

subtotal = 0
savings = 0
for prices in range(number_of_prices):
    price = float(input("Enter Price "))
    if price > 0:
        subtotal += price

    if price < 0:
        savings += price

grand_total = subtotal - savings
print("Report")
print(f"Subtotal: {subtotal}")
print(f"Savings:{savings}")
print(f"Grand Total:{grand_total}")

average_price = subtotal/number_of_prices
print(f"Average Item Price:{average_price}")
average_discount = savings/number_of_prices
print(f"Average Discount:{average_discount}")