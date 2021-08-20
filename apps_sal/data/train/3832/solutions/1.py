from itertools import islice


def A000166():
    (a, b, n) = (1, 0, 1)
    while True:
        yield a
        (a, b) = (b, n * (a + b))
        n += 1


all_permuted = dict(enumerate(islice(A000166(), 5000))).get
