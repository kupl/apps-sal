def divisors(n):
    cnt = 0
    for num in range(1,n):
        if n % num == 0:
            cnt+=1
    return cnt+1
