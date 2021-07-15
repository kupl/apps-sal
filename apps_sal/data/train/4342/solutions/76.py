def no_space(x):
    lista = []
    result = ''
    for n in x:
        if n != ' ':
            lista.append(n)
    for n in lista:
        result += n
    return result
