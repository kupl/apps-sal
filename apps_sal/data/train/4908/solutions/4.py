def epidemic(tm, n, s0, i0, b, a):
    S = {0: s0}
    I = {0: i0}
    dt = tm / n
    for k in range(n):
        S[k + 1] = S[k] - tm / n * b * S[k] * I[k]
        I[k + 1] = I[k] + tm / n * (b * S[k] * I[k] - a * I[k])
    return int(I[max(I, key=lambda key: I[key])])
