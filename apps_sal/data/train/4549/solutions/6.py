def lemming_battle(k, a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    while a and b:
        for i, j in zip(a[:k], b[:k]):
            temp = max(i, j)
            a.remove(i)
            b.remove(j)
            if i == j:
                continue
            if temp == i:
                a.append(i - j)
            elif temp == j:
                b.append(j - i)
        a.sort(reverse=True)
        b.sort(reverse=True)
    return [[f"Green wins: {' '.join(map(str, a))}", f"Blue wins: {' '.join(map(str, b))}"][len(b) > 0], "Green and Blue died"][len(a) == len(b)]
