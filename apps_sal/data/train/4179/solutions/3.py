def game(n):
    m = n * n
    if (m % 2 == 0):
        return [m // 2] 
    else: return [m, 2]
