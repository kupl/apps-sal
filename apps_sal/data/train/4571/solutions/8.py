from math import log
decompose = d = lambda n, k=[], i=2: n < i * i and [k, n] or d(n - i ** int(log(n, i)), k + [log(n, i) // 1], i + 1)
