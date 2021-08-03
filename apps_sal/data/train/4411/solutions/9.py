def find_missing_number(numbers):
    n = len(numbers) + 1
    expected = (n * (n + 1)) / 2
    return expected - sum(numbers)
