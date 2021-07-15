def arr(n=''):
    if n == '':
        return []
    else:
        lista = []
        n = int(n)
        for i in range(n):
            caracter =int(i)
            lista.append(caracter)
        return lista
