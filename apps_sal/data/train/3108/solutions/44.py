def multi_table(n):
    m = []
    for i in range(1, 11):
        m.append(f"{i} * {n} = {i * n}")
    w = "\n".join(m)
    return w
