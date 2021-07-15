def split_and_add(numbers, n):
    for _ in range(n):
        m, r = divmod(len(numbers), 2)
        numbers = list(map(sum, zip(r * [0] + numbers[:m], numbers[m:])))
    return numbers
