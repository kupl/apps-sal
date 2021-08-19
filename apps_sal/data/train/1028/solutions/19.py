t = int(input())
for w in range(t):
    n = int(input())
    m = n
    sm = digit = 0
    while n > 0:
        n = n // 10
        digit += 1
    n = m
    while m > 0:
        a = m % 10
        sm = sm + a ** digit
        m = m // 10
    if n == sm:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
