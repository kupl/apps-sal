def goldbach_partitions(n):
    def prime(a):
        if a == 2: return True
        if a < 2 or a % 2 == 0: return False
        return not any(a % x == 0 for x in range(3, int(a ** 0.5) + 1, 2))

    if n<4 or n%2!=0:
        return []
    if n==4:
        return ['2+2']
    res = []
    x = 3
    while True:
        y = n-x
        if x>y:
            return res
        if prime(y):
            res.append(str(x) + '+' + str(y))            
        x += 2
        while not prime(x):
            x += 2
