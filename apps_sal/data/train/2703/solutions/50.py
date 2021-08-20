def square_sum(numbers):
    sum = 0
    for number in numbers:
        sum = sum + abs(number ** 2)
    return sum
