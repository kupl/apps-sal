def pre_fizz(n):
    list = []
    while True:
        if n != 0:
            list.insert(0, n)
            n -= 1
        elif n == 0:
            break
    return list
