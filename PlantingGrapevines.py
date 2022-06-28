# Starting Out With Python 5th Edition: Chapter 2 - Exercise 13

# Input length of the row in feet
lengthOfRow = float(input('Enter length of the row in feet: '))

# Input the amount of space used by an end-post assembly in feet
amountOfSpaceAssembly = float(input('Enter the amount of space used by an end-post assembly in feet: '))

# Input the amount of space between the vines, in feet
amountOfSpaceBetweenVines = float(input('Enter the amount of space between vines in feet: '))

# Calculate amount of grapevines that will fit in each row
amountOfGrapevinesPerRow = int((lengthOfRow - 2 * amountOfSpaceAssembly) / (amountOfSpaceBetweenVines))

# Display amount of grapevines per row
print('Amount of grapevines per row:', amountOfGrapevinesPerRow)
