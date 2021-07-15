def prime_or_composite(n):
    from random import randrange
    if n == 2:
        return 'Probable Prime'
    if not n & 1:
        return 'Composite'

    def check(a , s , d , n):
        x = pow(a , d , n)
        if x == 1:
            return 'Probable Prime'
        for i in range(s - 1):
            if x == n - 1:
                return 'Probable Prime'
            x = pow(x , 2 , n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(2,20):
        a = randrange(2 , n)
        if not check(a , s , d , n):
            return 'Composite'
    return 'Probable Prime'
