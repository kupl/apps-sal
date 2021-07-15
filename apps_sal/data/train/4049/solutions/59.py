def monkey_count(n):
    z = 0
    liste = []
    while n != 0:
        n -= 1
        z  += 1
        liste.append(z) 
    return liste
