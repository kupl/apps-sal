def hotpo(n):
    count = 0
    while n!=1:
        n = n//2 if n%2==0 else 3*n+1
        count += 1
    return count
