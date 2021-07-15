def sum_triangular_numbers(n):
    x = 1
    y = 2
    z = []
    while len(z)<n:
        z.append(x)
        x+=y
        y+=1
    return sum(z)
