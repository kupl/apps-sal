def gen():
    while True:
        yield "1"
        yield "0"


def stringy(size):
    g = gen()
    return "".join(next(g) for _ in range(size))
