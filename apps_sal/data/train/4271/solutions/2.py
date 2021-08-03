TOME = dict(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1), 'M CM D CD C XC L XL X IX V IV I'.split()))
FRAC = dict(enumerate((".", ":", ":.", "::", ":.:", "S", "S.", "S:", "S:.", "S::", "S:.:"), 1))


def roman_fractions(i, f=0):
    if i < 0 or f < 0 or f == 12 or i > 5000:
        return "NaR"
    lst = []
    for v, r in TOME.items():
        n, i = divmod(i, v)
        if n:
            lst.extend([r] * n)
    if f:
        lst.append(FRAC[f])
    return ''.join(lst) or 'N'
