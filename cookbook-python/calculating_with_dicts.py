prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

# First way
print(sorted(zip(prices.values(), prices.keys()))[::-1])

# Second way
print("first: ", max(prices, key= lambda x: prices[x]), prices[max(prices, key= lambda x: prices[x])])
print("last: ", min(prices, key= lambda x: prices[x]), prices[min(prices, key= lambda x: prices[x])])
