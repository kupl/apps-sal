def create_array(n):
    g = []
    for x in range(n):
        g.append(x)
    g.append(n)
    return g[1:]
