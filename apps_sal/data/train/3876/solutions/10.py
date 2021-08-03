def find(n):
    return sum([ele for ele in range(3, n + 1, 3) if ele % 5 != 0]) + sum(range(5, n + 1, 5))
