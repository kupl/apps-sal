def recaman(n):
    seq = [0]
    seen = {0}
    for i in range(1, n + 1):
        x = seq[-1] - i
        if x < 0 or x in seen:
            x = seq[-1] + i
        seq.append(x)
        seen.add(x)
    return seq[-1]
