def divisible_by(numbers, divisor):
    lista = []
    for n in numbers:
        if n % divisor == 0:
            lista.append(n)
    return lista
