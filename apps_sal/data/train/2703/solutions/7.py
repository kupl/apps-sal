def square_sum(numbers):
    result = []
    for sqr in numbers:
        result.append(sqr ** 2)
    return sum(result)
