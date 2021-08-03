def square_sum(numbers):
    lista = []
    for valor in numbers:
        valor1 = valor * valor
        lista.append(valor1)
    lista = sum(lista)
    return lista
