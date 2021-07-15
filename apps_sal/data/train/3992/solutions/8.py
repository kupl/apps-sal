def is_happy(n):
    while n>=7:
        n = sum(int(x)**2 for x in str(n))
    return n==1
