def narc(n):
    ds = [int(c) for c in str(n)]
    return sum(d**len(ds) for d in ds) == n


def is_narcissistic(*ns):
    return (
        all((isinstance(n, int) and n >= 0) or (isinstance(n, str) and n.isdigit()) for n in ns) and
        all(map(narc, map(int, ns)))
    )
