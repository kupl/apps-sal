def difference_of_squares(n):
    return sum(el for el in range(n+1)) ** 2 - sum(el**2 for el in range(n+1))
