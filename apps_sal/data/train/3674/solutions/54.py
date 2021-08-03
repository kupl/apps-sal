def add_binary(a, b):
    itog = ''
    c = a + b
    while c != 1:
        itog = str(c % 2) + itog
        c = c // 2
    itog = '1' + itog
    return itog
