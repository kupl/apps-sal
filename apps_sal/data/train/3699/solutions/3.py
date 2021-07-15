def ranks(a):
    dict = {v: k for k, v in sorted(enumerate(sorted(a, reverse=True), start=1), reverse=True)}
    return [dict[i] for i in a]

