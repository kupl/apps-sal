def angle(n):
    if not n>=3:
        return 
    sum = 180
    for _ in range(n-3):
       sum = sum + 180
    return sum
