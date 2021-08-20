def transpose_two_strings(arr):
    p = arr[:]
    if len(p[0]) > len(p[1]):
        p[1] = p[1].ljust(len(p[0]))
    elif len(p[0]) < len(p[1]):
        p[0] = p[0].ljust(len(p[1]))
    return '\n'.join([f'{i} {j}' for (i, j) in zip(*p)])
