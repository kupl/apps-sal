def f(n):
    if type(n) == str:
        return None
    elif n < 0:
        return None
    if type(n) == float:
        return None
    if n == 0:
        return None
    suma = 0
    for i in range(n+1):
        suma+=i
    return suma
