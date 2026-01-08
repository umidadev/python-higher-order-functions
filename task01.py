numbers = [4, -2, 0, 7, -9, 3, -1, 5]

def is_even(x: int) -> bool:
    return x % 2 == 0

evens = filter(is_even, numbers)
print(list(evens))