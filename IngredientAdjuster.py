# Starting Out With Python 5th Edition: Chapter 2 - Exercise 10

# Define constants
COOKIES = 48
cups_of_sugar = 1.5
cups_of_butter = 1
cups_of_flour = 2.75

# Input number of cookies
number_of_cookies = int(input('Enter number of cookies: '))

# Calculate cookie ratio (total cookies / cookies)
cookie_ratio = number_of_cookies / COOKIES

# Calculate cookie ratio * cups of sugar
sugar = cookie_ratio * cups_of_sugar

# Calculate cookie ratio * cups of butter
butter = cookie_ratio * cups_of_butter

# Calculate cookie ratio * cups of flour
flour = cookie_ratio * cups_of_flour

# Display amount of cups needed for each ingredient
print(f'{sugar:.2f} cups of sugar, {butter:.2f} cups of butter, {flour:.2f} cups of flour')
