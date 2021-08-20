def reverse(a):
    lista = []
    li = list(a.split(' '))
    li.reverse()
    for i in li:
        if i != '':
            lista.append(i)
    return ' '.join(lista)
