# Starting Out With Python 5th Edition: Chapter 2 - Exercise 14

# Input amount of principal originally deposited
p = float(input('Enter the amount of principal originally deposited: '))

# Input the annual interest rate
r = float(input('Enter the annual interest rate: '))
r /= 100

# Input the number of years that the interest is compounded
n = float(input('Enter the number of years the interest is compounded: '))

# Input the number of years
t = float(input('Enter the number of years: '))

# Calculate amount and display
a = p * ((1 + (r/n))**(n*t))
print('After ', t, ' years $', format(a, ',.2f'), ' will be in the account', sep = '')