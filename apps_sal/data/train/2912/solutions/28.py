def find_multiples(integer, limit):
    # Your code here!
    lista = []
    for i in range(integer, limit + 1):
        lista.append(i)
    return list(filter(lambda numero: numero % integer == 0, lista))
