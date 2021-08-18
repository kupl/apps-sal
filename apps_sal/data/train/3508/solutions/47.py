def halving_sum(n):
    print(n)
    i = 1
    suma = 0
    resultado = 0
    while i < n:
        suma = n / i
        print((int(suma)))
        resultado = resultado + int(suma)
        i *= 2
    if(int(resultado) == 0):
        resultado = 1
        return(int(resultado))
    else:
        print((int(resultado)))
        return(int(resultado))
