def find(n):
    return sum(range(3,n+1,3)) + sum(x for x in range(5,n+1,5) if x % 3 != 0)
