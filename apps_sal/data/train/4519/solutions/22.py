def max_number(n):
    lista = [int(i) for i in str(n)]
    lista.sort(reverse=True)
    string = [str(i) for i in lista]
    result = int(''.join(string))
    return result
