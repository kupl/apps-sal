def factorsRange(n, m): return {x: sorted(set(__import__("itertools").chain(*((y, x / y)for y in range(2, int(x**.5) + 1)if not x % y)))) or ['None']for x in range(n, m + 1)}
