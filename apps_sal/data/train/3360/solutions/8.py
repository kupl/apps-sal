def get_chance(n, x, a):
    output = 1
    for i in range(0,a):
        if n - i == x:
            return 0
        output *= (n-x-i)/(n-i)
    return round(output,2)
