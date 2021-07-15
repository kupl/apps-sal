def sum_mul(n, m):
    print(n)
    print(m)
    numbers = list()
    
    if m <= 0 or n <= 0:
        return "INVALID"
    if n > m:
        return 0
    if m<n:
        return "INVALID"
    
    
    
    i = 1
    while i < m:
        if n * i < m:
            numbers.append(n * i)
            i = i + 1
        else:
            break
    
    return sum(numbers)
