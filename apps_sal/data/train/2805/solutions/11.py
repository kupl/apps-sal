def productFib(prod):
    i = 0
    j = 1
    while i * j < prod:
        i, j = j, i+j
    return [ i, j, i*j == prod ]

