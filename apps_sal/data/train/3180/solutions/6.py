def trotter(n):
    if not n:
        return "INSOMNIA"

    seen, o = set(str(n)), n
    while len(seen) != 10:
        n += o
        seen |= set(str(n))
    return n
