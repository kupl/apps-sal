def create_array(n):
    lista = []
    for i in range(n):
        lista.append(n)
        n = n - 1
    lista.reverse()
    return lista
    

