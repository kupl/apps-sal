def halving_sum(n): 
    # your code here
    print(n)
    i = 1
    suma = 0
    resultado = 0
    while i < n:
        #print(i)
        suma = n/i
        print((int(suma)))
        resultado = resultado + int(suma)
        #print(int(resultado))
        #print(i)
        i *= 2
        #print(i)
    if(int(resultado) == 0):
        resultado = 1
        return(int(resultado))
    else:
        print((int(resultado)))
        return(int(resultado))

