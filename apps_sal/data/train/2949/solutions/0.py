def split_and_add(numbers, n):
    for _ in range(n):
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]
        numbers = [a + b for a, b in zip((len(right) - len(left)) * [0] + left, right)]
        if len(numbers) == 1:
            return numbers
    return numbers

