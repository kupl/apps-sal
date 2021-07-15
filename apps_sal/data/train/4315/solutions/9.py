def sum_them(n):
    return (1 << n) - 1 << (n - 1 if n else 0)
    

