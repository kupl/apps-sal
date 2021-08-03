def split_exp(n):
    o = n.index(".") if "." in n else len(n)

    def split(i, c): return "{}{}{}".format(
        "" if o - i > 0 else ".{}".format("0" * (- (o - i + 1))),
        c,
        "0" * (o - i - 1))
    return [split(i, c) for i, c in enumerate(n) if i - o != 0 if float(split(i, c)) != 0]
