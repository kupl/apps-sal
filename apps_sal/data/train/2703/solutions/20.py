def square_sum(numbers):
    i = 0
    sum = 0
    while i < len(numbers):
        sum = sum + numbers[i] ** 2
        i = i + 1
    return sum
