text = ["apple", "34", "banana", "100", "abc", "75"]

result = list(filter(
    lambda x: x.isdigit(),
    text
))

print(result)