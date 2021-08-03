def get_sum(a, b):
    soma = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a + 1):
            soma += i
        return soma
    else:
        for i in range(a, b + 1):
            soma += i
        return soma
