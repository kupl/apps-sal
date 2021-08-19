def find_missing_number(numbers):
    x = len(numbers)
    total = sum(numbers)
    rest = (x + 1) * (x + 2)
    rest = rest / 2
    missing = rest - total
    return missing
