def max_tri_sum(numbers: list):
    numbers = set(numbers)
    s = 0
    for _ in range(3):
        i = max(numbers)
        s += i
        numbers.remove(i)
    return s
