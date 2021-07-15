def div_con(x):
    return sum(-int(i) if isinstance(i, str) else i for i in x)
