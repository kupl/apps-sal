def digitize(n):
    lista = list(str(n))
    lista.reverse()
    int_list = []
    for i in lista:
        int_list.append(int(i))
    
    return int_list
