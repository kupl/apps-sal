def seven(m):
    lenght = len(str(m))
    steps = 0
    while lenght > 2:
        x = m // 10
        y = m % 10
        m = x - 2*y
        steps += 1
        lenght = len(str(m))
    return m, steps
    
            

