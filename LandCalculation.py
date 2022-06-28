# Starting Out With Python 5th Edition: Chapter 2 - Exercise 3

# Define constant for square feet per acre of land
SQUARE_FT_PER_ACRE = 43560

# Input total square feet in tract of land
total_square_ft = float(input('Enter total square feet in tract of land: '))

# Calculate total square feet / square feet per acre and display
print(f'Number of acres in tract of land is {total_square_ft / SQUARE_FT_PER_ACRE: ,.2f}')
