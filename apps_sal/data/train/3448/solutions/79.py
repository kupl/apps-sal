def f(n):
    print(n) 
    if isinstance(n, int) and n > 0:
        x = 0
        y = 0
        while x <= n:
            y += x
            x += 1 
        return y
    else:
        return None
