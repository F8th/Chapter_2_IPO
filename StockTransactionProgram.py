# Starting Out With Python 5th Edition: Chapter 2 - Exercise 12

# Define constants
NUMBER_OF_SHARES = 2000
PRICE_PER_SHARE = 40
COMMISSION = 0.03

# Calculate number of shares * price per share and display
amountPaidForStock = NUMBER_OF_SHARES * PRICE_PER_SHARE
print('Amount of money Joe paid for the stock: $', amountPaidForStock, sep = '')

# Calculate the amount of commission (price per share * number of shares * commission) and display
commissionPaidForStock = amountPaidForStock * COMMISSION
print('Amount of commission (3%) Joe paid when purchasing the stock: $', commissionPaidForStock, sep = '')

# Calculate the amount for which Joe sold the stock at $42.75 per share and display
amountSoldForStock = 42.75 * NUMBER_OF_SHARES
print('Amount for which Joe sold the stock at $42.75 per share: $', amountSoldForStock, sep = '')

# Calculate the amount of commission paid after selling the stock
commissionForStockSold = amountSoldForStock * COMMISSION
print('Amount of commission (3%) Joe paid when reselling the stock: $', commissionForStockSold, sep = '')

# Display amount of money Joe had left
profit = amountSoldForStock - amountPaidForStock - (commissionPaidForStock + commissionForStockSold)
print('Profit: $', profit, sep = '')
