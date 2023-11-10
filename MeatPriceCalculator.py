#Added a Tip amount option to show creativity.

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of a adult meal? "))
child_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))

child_price = child_meal_price * child_count
adult_price = adult_count * adult_meal_price
subtotal_price = adult_price + child_price

print()
print("Subtotal:$", subtotal_price)
print()

tax_rate = float(input("What is the sales tax rate? "))
tax_add = round(((tax_rate / 100) * subtotal_price),2)
print("Sales tax:$", tax_add)

total_price = round((tax_add + subtotal_price), 2)
print("Total:$", total_price)
print()

tip_pecent = float(input("What percent of a tip do you want to leave? "))
tip_amount = round(((tip_pecent / 100) * total_price), 2)
total_price += tip_amount
print("Tip amount:$", tip_amount)
print("Final price:$", total_price)
print()

pay = float(input("What is the payment amount? "))
change = round((pay - (total_price + tip_amount)), 2)
print("Change:$", change)