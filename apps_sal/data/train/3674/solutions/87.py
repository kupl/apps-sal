def add_binary(a, b):
    z = a + b
    m = []
    while(z != 0):
        m.append(z % 2)
        z = z // 2
    for i in m[::-1]:
        z = z * 10 + i
    return str(z)
