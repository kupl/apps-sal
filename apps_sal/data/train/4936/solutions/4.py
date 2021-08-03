def reverse(lst):
    out = list()
    while lst:
        out.append(lst.pop(-1))
    return out
