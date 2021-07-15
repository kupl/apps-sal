def modified_sum(a, n):
    return sum(i ** n for i in a) - sum(a)
