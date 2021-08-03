def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n - k) // (k + 1))
    return line


def reduce_pyramid(a):
    x = len(a) - 1
    C = pascal(x)
    s = 0
    for i, v in enumerate(a):
        s += C[i] * v
    return s
