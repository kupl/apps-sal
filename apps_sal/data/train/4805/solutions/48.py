def check(seq, elem):
    return {k:True for v,k in enumerate(seq)}.get(elem, False)

