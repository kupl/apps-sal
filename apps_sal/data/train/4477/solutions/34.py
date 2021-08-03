def reverse_number(n):
    aux = n
    reverso = 0
    while abs(n) > 0:
        ultimoDigito = abs(n) % 10
        n = abs(n) // 10
        reverso = reverso * 10 + ultimoDigito
    if aux > 0:
        return reverso
    else:
        return reverso * (-1)
