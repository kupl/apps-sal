
def difference_of_squares(n):
    num1 = sum(i for i in range(1, n + 1))**2
    num2 = sum(i**2 for i in range(1, n + 1))
    return abs(num1 - num2)
