def s(n):
    xs = [1]
    yield xs
    for i in range(n):
        while True:
            xs = [a ^ b for (a, b) in zip([0] + xs, xs + [0])]
            yield xs
            if all(xs):
                break


def sierpinski(n):
    xss = list(s(n))
    width = len(xss) * 2 - 1
    return '\n'.join((' '.join((' *'[x] for x in xs)).center(width) for xs in xss))
