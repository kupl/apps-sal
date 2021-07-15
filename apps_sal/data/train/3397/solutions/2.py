def grille(m, c):
    return "".join(i[0] for i in zip(m[::-1],bin(c)[2:][::-1]) if i[1]=="1")[::-1]
