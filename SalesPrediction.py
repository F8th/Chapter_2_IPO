# Starting Out With Python 5th Edition: Chapter 2 - Exercise 2

# Define constant for return on sales
RETURN_ON_SALES = 0.23

# Input amount of sales
projected_sales = float(input('Enter amount of projected sales: '))

# Calculate projected sales * return on sales and display the amount
print(f'Projected amount is {projected_sales * RETURN_ON_SALES: ,.2f}')
