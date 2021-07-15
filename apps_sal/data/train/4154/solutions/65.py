#def is_triangle2(a, b, c):
#    lista = sorted([a,b,c])
#    if lista[0] + lista[1] > lista[2]:
#        return True
#    return False

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
