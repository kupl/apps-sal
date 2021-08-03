def f(n):
    if isinstance(n, int) == True:
        if n > 0:
            sum = 0
            for num in range(0, n + 1, 1):
                sum = sum + num
            return sum
        else:
            None
    else:
        return None
