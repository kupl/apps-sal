for _ in range(int(input())):
    n = int(input())
    x = len(str(n))
    t, s = n, 0
    while(n):
        s += (n % 10)**x
        n //= 10
    if t == s:
        print('FEELS GOOD')
    else:
        print('FEELS BAD')
