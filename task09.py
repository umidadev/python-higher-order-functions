names = ["Ali", "Valijon", "Sami", "Diyorbek"]

longlest_name = max(
    names,
    key = lambda name: len(name)
)

print(longlest_name)