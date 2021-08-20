def cycle(i):
    if i % 2 == 0 or i % 5 == 0:
        return -1
    gen = 10
    n = 1
    while gen % i != 1:
        gen = gen % i * 10
        n = n + 1
    return n
