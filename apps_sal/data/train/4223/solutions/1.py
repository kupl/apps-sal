def comp(a1, a2):
    return None not in (a1, a2) and [i * i for i in sorted(a1)] == sorted(a2)
