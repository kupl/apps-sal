def array_madness(a, b):
    kv = 0
    kub = 0
    for i in a:
        kv += i ** 2
    for j in b:
        kub += j ** 3
    return kv > kub
