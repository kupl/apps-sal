def args_count(*args, **kwargs):
    lista = []
    for i in args:
        lista.append(str(i))
    for j in kwargs:
        lista.append(j)
    return len(lista)
