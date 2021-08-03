def maximum_product_of_parts(n):
    n = str(n)
    s = []
    for i in range(1, len(n) - 1):
        for h in range(i + 1, len(n)):
            f, m, l = int(n[0:i]), int(n[i:h]), int(n[h:])
            s.append(f * m * l)
    return max(s)
