def sum_cubes(n):
    x= 1
    total = 0
    while x<=n:
        total+= x**3
        x+=1
    return total
