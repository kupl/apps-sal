def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    elif n > m:
        return 0
    else:
        suma = 0
        for i in range(0, m, n):
            suma = suma + i
        return suma
