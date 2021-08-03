def solve(a, b):

    e = [i for i in a if i not in b]
    f = [i for i in b if i not in a]

    return "".join(e) + "".join(f)
