def max_tri_sum(numbers):
    numbers = set(numbers)
    max_sum = 0
    for i in range(3):
        n = max(numbers)
        numbers.remove(n)
        max_sum += n
    return max_sum
