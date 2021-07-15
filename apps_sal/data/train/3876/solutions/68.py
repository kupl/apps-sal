def find(n):
    em = []
    for i in range(n+1):
        if i % 3 == 0:
            em.append(i)
        elif i % 5 == 0:
            em.append(i)
    return sum(em)
