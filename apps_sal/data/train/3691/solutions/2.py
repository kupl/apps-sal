from itertools import chain

def get_a_down_arrow_of(n):
    result = []
    for i in range(n, 0, -1):
        row = " " * (n - i) + "".join(str(d % 10) for d in chain(range(1, i), range(i, 0, -1)))
        result.append(row)
    return "\n".join(result)
