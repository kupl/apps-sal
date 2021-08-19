from string import ascii_lowercase
ns = {x: i for (i, x) in enumerate(ascii_lowercase, 1)}


def short(xs):
    for i in range(1, len(xs)):
        if all((len(set(xs[j::i])) == 1 for j in range(i))):
            return xs[:i]
    return xs


def find_the_key(message, code):
    xs = [a - b for (a, b) in zip(code, map(ns.get, message))]
    return int(''.join(map(str, short(xs))))
