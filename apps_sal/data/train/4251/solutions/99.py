def difference_of_squares(n):
    lst1 = [(x + 1) for x in range(n)]
    lst2 = [(x + 1)**2 for x in range(n)]
    return abs(sum(lst2) - (sum(lst1))**2)
