from itertools import chain


def pattern(n):
    line = list(i + 1 for i in range(n))
    return "\n".join("".join(str(x) for x in chain(line[i:], line[:i])) for i in range(n))
