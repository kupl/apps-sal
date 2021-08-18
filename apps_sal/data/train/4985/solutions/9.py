d = {"Bb": "A
q = ["A", "A


def transpose(a, n):
    return [q[(q.index(d.get(x, x)) + n) % len(q)] for x in a]
