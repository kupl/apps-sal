def four_piles(n,y):       
    x = y * n / (y**2 + 2*y + 1)
    return [x + y, x - y, x * y, x / y] if int(x) == x and x - y > 0 else []
