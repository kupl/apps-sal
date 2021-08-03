import math


def bases(n):
    n = int(n)
    if n == 0:
        return('0')
    elif n == 1:
        return('INFINITY')
    else:
        sumas = 1
        i = 2
        while i < n:
            arreglo = primer_digito(n, i)
            potencia = arreglo[1]
            primer = arreglo[0]
            resto = n - (i ** potencia)
            if primer == 1 and potencia == 1:
                sumas += resto
                i += resto
            elif primer == 1:
                sumas += 1
                i += 1
            else:
                i += 1
        return sumas


def primer_digito(numero, base):
    potencia = int(math.log(numero, base))
    primer = numero // (base ** potencia)
    if primer >= base:
        primer = primer / base
        potencia += 1
    arreglo = [primer, potencia]
    return arreglo


casos = input()
for i in range(int(casos)):
    numero = input()
    print(bases(numero))
