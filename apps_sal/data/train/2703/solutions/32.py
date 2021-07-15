def square_sum(numbers):
    lista = []
    for i in numbers:
        i = i**2
        lista.append(i)
    return sum(lista)
