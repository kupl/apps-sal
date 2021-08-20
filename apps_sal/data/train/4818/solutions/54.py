def solution(a, b):
    if len(a) > len(b):
        sumar = b + a + b
    else:
        sumar = a + b + a
    return sumar
