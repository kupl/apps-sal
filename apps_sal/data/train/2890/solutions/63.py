def multiples(m, n):
    x = 1
    temp = 0
    final = []
    while x <= m:
        temp = x * n
        final.append(temp)
        print(final)
        x = x + 1
    return final
