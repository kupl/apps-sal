def hotpo(n):
    times = 0
    while True:
        if n == 1: break
        n = n//2 if not n%2 else n*3 + 1
        times += 1

    return times
