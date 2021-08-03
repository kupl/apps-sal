def square_sum(numbers):
    squared = []
    for i in numbers:
        x = i ** 2
        squared.append(x)
    y = sum(squared)
    return y


square_sum([0, 3, 4, 5])
