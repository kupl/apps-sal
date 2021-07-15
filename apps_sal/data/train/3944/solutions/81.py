def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    else:
        x=0
        for i in range(0,n+1):
            x+=i*(i+1)/2
        return int(x)
