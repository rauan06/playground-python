###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'

# Slices for extracting shares and price
SHARES_SLICE = slice(20, 23)
PRICE_SLICE = slice(31, 37)

# Extracting values using the slices
shares = int(record[SHARES_SLICE])
price = float(record[PRICE_SLICE])

# Calculating cost
cost = shares * price

print(cost)  # Output should be 100 * 513.25 = 51325.0

a = "Hello World!"
print(PRICE_SLICE.indices(len(a)))
