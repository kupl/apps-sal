def decrypt(s):
    x, l = int(s), 10**len(s)
    for i in range(l + x, 11 * l + x, l):
        if not i % 11:
            return str(i // 11)
    return "impossible"
