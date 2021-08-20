def modified_sum(a, n):
    sum = 0
    for x in a:
        sum += x ** n - x
    return sum
