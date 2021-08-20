def add_binary(a, b):
    suma = bin(a + b)
    suma = suma.split('0b')
    return str(suma[1])
