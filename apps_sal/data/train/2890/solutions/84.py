def multiples(m, n):
    x = []
    for num_jumps in range(1, m + 1):
        x.append(n * num_jumps)
    return x


