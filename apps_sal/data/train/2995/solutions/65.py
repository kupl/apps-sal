def sum_mul(n, m):
    sum = 0
    counter = 0
    if(m <= 0 or n <= 0):
        return "INVALID"
    while counter < m:
        sum += counter
        counter += n
    return sum
