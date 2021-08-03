def divisors(n):
    lista = 0
    for i in range(1, n + 1):
        if n % i == 0:
            lista += 1
    return lista
