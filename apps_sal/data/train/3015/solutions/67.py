L = {}
for s in ('AMEX_34 37_15', 'Discover_6011_16', 'Mastercard_51 52 53 54 55_16', 'VISA_4_13_16'):
    a, b, *c = s.split('_')
    L[a] = b.split(' '), tuple(map(int, c))


def get_issuer(n):
    s = str(n)
    for k in L:
        ps, ls = L[k]
        if len(s) in ls and any(s.startswith(p) for p in ps):
            return k
    return 'Unknown'
