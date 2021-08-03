def string_func(s, x):
    l = len(s)
    cyc = x % life(l)
    order = list(s)
    string = list(s)

    c = 0
    for i in range(l - 1, -1 + l // 2, -1):
        order[c] = i
        c += 2
    c = 1
    for i in range(0, l // 2, 1):
        order[c] = i
        c += 2

    return "".join(sort(order, string, cyc))


def sort(schema, string, times):
    for x in range(times):
        result = []
        for i in range(len(string)):
            result.append(string[schema[i]])
        string = result
    return string


def life(n):
    if n <= 1:
        return 1
    m = 1
    while True:
        a = (2 ** m) % (2 * n + 1)
        if a == 1 or a == 2 * n:
            return m
        m = m + 1
