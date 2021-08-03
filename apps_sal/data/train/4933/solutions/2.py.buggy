In [28]: UP_LOW = (str.upper, str.lower)
In [29]: def random_case(x): return ''.join(choice(UP_LOW)(c) for c in x)
In [30]: %timeit random_case(s)
723 ms ± 14 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

