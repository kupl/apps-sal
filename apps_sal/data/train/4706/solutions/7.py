def split_exp(n):
    o = n.index(".") if "." in n else len(n)
    split = lambda i, c: "{}{}{}".format(
        "" if o - i > 0 else ".{}".format("0" * (- (o - i + 1))),
        c,
        "0" * (o - i - 1))
    return [split(i, c) for i, c in enumerate(n) if i - o != 0 if float(split(i, c)) != 0]
