# Starting Out With Python 5th Edition: Chapter 2 - Exercise 4

# Define constant for sales tax
SALES_TAX = 0.07

# Input price for five items
item1 = float(input('Item 1 Price: '))
item2 = float(input('Item 2 Price: '))
item3 = float(input('Item 3 Price: '))
item4 = float(input('Item 4 Price: '))
item5 = float(input('Item 5 Price: '))

# Calculate subtotal of the sale
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate sales tax amount
sales_tax_amount = subtotal * SALES_TAX

# Display subtotal, sales tax, and total
print(f'\nSubtotal: {subtotal:,.2f}\n' f'Sales Tax: {sales_tax_amount:,.2f}', f'\nTotal: {subtotal + sales_tax_amount}')
