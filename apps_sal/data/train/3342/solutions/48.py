def pattern(n):
    imprimir = []
    for i in range(1,n + 1):
        patron = (str(i)) *i
        imprimir.append(patron)
        '\n'.join(imprimir)
    return '\n'.join(imprimir)
