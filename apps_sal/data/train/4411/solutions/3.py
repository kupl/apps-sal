def find_missing_number(numbers):
    return sum(list(range(1, len(numbers) + 2))) - sum(numbers)
