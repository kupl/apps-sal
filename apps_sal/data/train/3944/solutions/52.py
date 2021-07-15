def sum_triangular_numbers(n):
    if n < 0:
        return 0
    else:
        sum = 0
        for i in range(1, n + 1): 
            x = ((i ** 2 + i)//2)
            sum += x 
        return sum
