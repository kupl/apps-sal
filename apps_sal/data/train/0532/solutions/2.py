def fib(n):
    s1, s2 = 1, 2
    if n == 1:
        return s1
    elif n == 2:
        return s2
    else:
        for i in range(2, n):
            s3 = (s1 + s2) % 15746
            s1 = s2
            s2 = s3
        return s2 % 15746


try:
    n = int(input())
    z = fib(n)
    print(z)

except:
    pass
