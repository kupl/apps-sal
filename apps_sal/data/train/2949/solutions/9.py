def split_and_add(numbers, n):
    from itertools import zip_longest
    for i in range(n):
        length = len(numbers) // 2
        numbers = list(reversed([x + y for (x, y) in zip_longest(reversed(numbers[0:length]), reversed(numbers[length:]), fillvalue=0)]))
    return numbers
