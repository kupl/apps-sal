def is_triangle(a, b, c):
    x = max(a, b, c)
    lista = [a, b, c]
    lista.remove(x)
    if x < sum(lista):
        return True
    else:
        return False
