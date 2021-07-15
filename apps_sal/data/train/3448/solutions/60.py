def f(n):
    if isinstance(n, int) == False or n <= 0:
        return None
    else:
        sum = 0
        for i in range(1, n+1):
            sum += i
        return sum

