def simplify(n):
    sq = next(k for k in range(int(n**0.5), 0, -1) if n % (k * k) == 0)
    rt = n // (sq * sq)
    return str(sq) if rt == 1 else f"{sq if sq > 1 else ''} sqrt {rt}".strip()


def desimplify(s):
    rt, _, sq = (int(n.replace("sqrt", "") or 1) for n in s.partition("sqrt"))
    return rt * rt * sq
