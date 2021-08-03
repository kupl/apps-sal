def xMasTree(n): return (lambda part: part + [part[0], part[0]])(["".join(["_" * (n - i - 1), "#" * (2 * i + 1), "_" * (n - i - 1)]) for i in range(n)])
