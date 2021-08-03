def f(n):
    if isinstance(n, int) == True:
        sum = 0
        if n > 0:
            for i in range(n + 1):
                sum += i
            return sum
        else:
            return None
    else:
        return None
