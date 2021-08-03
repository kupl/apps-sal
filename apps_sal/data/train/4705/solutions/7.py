def find_a_b(n, c): return (list(filter(lambda x: x[0] * x[1] == c, [list(e) for e in __import__("itertools").combinations(n, 2)])) + [None])[0]
