def binary_simulation(s, q):
    x, l, result = int(s, 2), len(s), []
    for op in q:
        if op[0] == 'I':
            i, j = op[1:]
            x ^= (1 << j-i+1)-1 << l-j
        else:
            result.append(str(x >> l-op[1] & 1))
    return result
