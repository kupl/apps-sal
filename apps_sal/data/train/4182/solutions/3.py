def survivor(n):
    print('look for %s' % n)
    last = 0
    for i in range(2, n):
        if last == n:
            return True
        print(n)
        if n % i == 0:
            return False
        else:
            last = n
            n = n - n // i
    return True
