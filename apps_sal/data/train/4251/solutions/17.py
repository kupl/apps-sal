def difference_of_squares(x):
    return sum(i * i * (i - 1) for i in range(x + 1))
