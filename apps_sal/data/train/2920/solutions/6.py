def pattern(n):
    (out, s) = ([], '')
    for i in reversed(range(1, n + 1)):
        s += str(i)
        out.append(s)
    return '\n'.join(out)
