def list_squared(m, n):
    output = []
    for i in range(m, n):
        div = set()
        for d in range(1, int(i**0.5) + 1):
            if i % d == 0:
                div.add(d)
                div.add(i / d)
        sumsqdiv = sum([a * a for a in div])
        if (sumsqdiv**0.5).is_integer():
            output.append([i, sumsqdiv])
    return output
