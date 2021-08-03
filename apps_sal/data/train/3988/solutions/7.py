from itertools import groupby as g
def encode(s): return "".join("%s%s" % (sum(1 for _ in v), k) for k, v in g(s))
def decode(s): return "".join(int(d) * c for d, c in zip(*[iter("".join(v) for _, v in g(s, key=str.isdigit))] * 2))
