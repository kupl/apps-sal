def next_num(n):
    n += 1
    while n <= 3608528850368400786036725:
        pr = ifpol(n)
        if pr == True:
            return n
        else:
            s = len(str(n))
            num = 10 ** (s - pr)
            n = (n // num + 1) * num


def ifpol(n):
    s = len(str(n))
    for i in range(1, s + 1):
        if n // 10 ** (s - i) % i != 0:
            return i
    return True
