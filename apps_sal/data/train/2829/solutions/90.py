def array_madness(a, b):
    x = 0
    y = 0
    for i in a:
        x += i ** 2
    for c in b:
        y += c ** 3
    return x > y
