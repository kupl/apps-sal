def square_sum(numbers):
    total = 0
    for n in range(0, len(numbers)):
        total = total + numbers[n]**2
    return total
