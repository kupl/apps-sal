def split_and_add(numbers, n):
    arr = numbers[:]
    for _ in range(n):
        mid, rest = divmod(len(arr), 2)
        arr = [a + b for a, b in zip(rest * [0] + arr[:mid], arr[mid:])]
    return arr
