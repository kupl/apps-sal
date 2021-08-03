def find_missing_number(numbers):
    t1 = sum(numbers)
    t2 = sum(range(1, len(numbers) + 2))
    return (t2 - t1)
