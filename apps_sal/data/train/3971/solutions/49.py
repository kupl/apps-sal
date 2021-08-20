def tidyNumber(n):
    ns = str(n)
    return all((a <= b for (a, b) in zip(ns, ns[1:])))
