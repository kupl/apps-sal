array_mash = lambda *a, c=__import__("itertools").chain: list(c(*zip(*a)))
