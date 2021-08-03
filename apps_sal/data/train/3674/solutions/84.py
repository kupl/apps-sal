def add_binary(a, b):
    somme = a + b
    binaire = ''
    i = 0
    while somme >= 2**(i + 1):
        i += 1
    while i >= 0:
        if somme >= 2**i:
            binaire = binaire + str(1)
            somme = somme - (2**i)
        else:
            binaire = binaire + str(0)
        i -= 1
    return binaire
