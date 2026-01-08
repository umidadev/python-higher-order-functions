prices= ["$120", "$340", "$50", "$90"]

result = map(
    lambda price: prices.replace('$', ""),
    prices
)

print(result)