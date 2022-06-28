# Starting Out With Python 5th Edition: Chapter 2 - Exercise 11

# Input number of males
number_of_males = int(input('Enter number of males: '))

# Input number of females
number_of_females = int(input('Enter number of females: '))

# Calculate percentage of males
percentage_of_males = number_of_males / (number_of_males + number_of_females)

# Calculate percentage of females
percentage_of_females = number_of_females / (number_of_males + number_of_females)
# Display results
print('Total Students:', number_of_males + number_of_females)
print(f'Males: {percentage_of_males:.0%}')
print(f'Females: {percentage_of_females:.0%}')
