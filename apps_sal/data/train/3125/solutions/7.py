def solve(n):
    if (n%2 == 0 and n%4 != 0) or n == 1 or n == 4:
        return -1
    for i in range(n-1):
        if ((n + (i+1)**2)**0.5)%1 == 0:
            return (i+1)**2

