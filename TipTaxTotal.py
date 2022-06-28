# Starting Out With Python 5th Edition: Chapter 2 - Exercise 8

# Define constants
TIP_PERCENT = 0.18
SALES_TAX = 0.07

# Input amount of meal purchased
amount = float(input('Enter amount of meal purchased: '))

# Calculate total amount
total_amount = amount + (amount * TIP_PERCENT) + (amount * SALES_TAX)

# Display amount * tip percentage
print(f'Amount of 18% percent tip is {amount * TIP_PERCENT:.2f}')

# Display amount * sales tax
print(f'Amount of 7% sales tax {amount * SALES_TAX:.2f}')

# Display total amount
print(f'The total amount is {total_amount:.2f}')