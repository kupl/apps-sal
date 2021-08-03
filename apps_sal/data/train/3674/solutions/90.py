def add_binary(a, b):
    suma = a + b
    temp = ''
    while suma > 0:
        temp = str(suma % 2) + temp
        suma = suma // 2
    return temp
