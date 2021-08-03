def f(n):
    sum = 0
    if isinstance(n, int) == True:
        if n > 0:
            for i in range(n):
                i = i + 1
                sum += i
            return sum
        else:
            return None
    else:
        return None
