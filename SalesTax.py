# Starting Out With Python 5th Edition: Chapter 2 - Exercise 6

# Define constants
STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025

# Input amount of purchase
amount = float(input('Enter amount of purchase: '))

# Calculate total sales tax
total_sales_tax = (amount * STATE_SALES_TAX) + (amount * COUNTY_SALES_TAX)

# Display the amount of purchase
print(f'Amount of purchase is {amount:,.2f}')

# Display state amount * state sales tax
print(f'State sales tax is {amount * STATE_SALES_TAX:,.2f}')

# Display amount * county sales tax
print(f'County sales tax is {amount * COUNTY_SALES_TAX:,.2f}')

# Display state sales tax + county sales tax
print(f'Total sales tax is {total_sales_tax:,.2f}')

# Display amount + total sales tax
print(f'Total of the sale is {amount + total_sales_tax:,.2f}')