def square_sum(numbers):
    numbers_ = 0
    for i in range(0, len(numbers)):
        numbers_ += numbers[i] ** 2
    return numbers_
