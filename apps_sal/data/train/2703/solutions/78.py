def square_sum(numbers):
    sum = 0
    if numbers:
        for num in numbers:
            sum += num * num
    return sum
