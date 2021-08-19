def cycle(n):
    if n % 5 == 0 or n % 2 == 0:
        return -1
    (remainders, r) = ([1], 0)
    while r != 1:
        r = remainders[-1] * 10 % n
        remainders.append(r)
    return len(remainders) - 1
