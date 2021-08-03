def find_missing_number(numbers):
    a = [False for i in range(len(numbers) + 1)]
    for i in numbers:
        a[i - 1] = True
    return a.index(False) + 1
