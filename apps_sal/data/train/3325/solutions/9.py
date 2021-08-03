def most_common(s): return "".join("".join(x[2] for x in y) for _, y in __import__("itertools").groupby(sorted((-s.count(x), i, x) for i, x in enumerate(s)), lambda x: x[0]))
