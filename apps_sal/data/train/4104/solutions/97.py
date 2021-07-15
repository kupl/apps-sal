def max_tri_sum(numbers):
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    numbers = numbers[0:3]
    return sum(numbers)
