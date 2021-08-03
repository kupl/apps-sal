def operator_insertor(total):
    q = [(total, "123456789", 0)]
    while q:
        s, n, d = q.pop(0)
        if int(n) == s:
            return d
        for i in range(0, len(n) - 1):
            n1 = int(n[0:i + 1])
            n2 = n[i + 1:]
            q.append((s - n1, n2, d + 1))
            q.append((n1 - s, n2, d + 1))
