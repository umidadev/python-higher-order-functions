nums = list(range(1, 21))

evens = filter(
    lambda x: x % 2 == 0,
    nums  
)

squared_nums = map(
    lambda x: x ** 2,
    evens
)

print(list(squared_nums))