def find(n):
    l = []
    calc = 0
    for x in range(n + 1):
        if x % 3 == 0:
            l.append(x)
            
        if x % 5 == 0:
            l.append(x)
    l = list(set(l))
    for y in range(len(l)):
        calc = calc + l[y]
    return calc
