def binary_pyramid(m, n):
    return f"{sum(int(f'{x:b}') for x in range(m, n+1)):b}"
