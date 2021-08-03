def pre_fizz(n):
    pre_fizz = []

    while n != 0:
        pre_fizz.append(n)
        n -= 1

    pre_fizz.sort()

    return pre_fizz
