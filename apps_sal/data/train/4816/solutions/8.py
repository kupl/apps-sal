def mutations(s):

    def flip(c):
        return {'B': 'W', 'W': 'B'}[c]

    def recurse(ss, n, acc):
        if not ss:
            if n > 0:
                yield ''.join(acc)
        else:
            yield from recurse(ss[1:], n, acc + [ss[0]])
            if n < 2:
                yield from recurse(ss[1:], n + 1, acc + [flip(ss[0])])
    yield from recurse(s, 0, [])


def child(bird1, bird2):
    possible = set(mutations(bird1))
    return bird2 in possible


def grandchild(bird1, bird2):
    possible = set((grand_child for child in mutations(bird1) for grand_child in mutations(child)))
    return bird2 in possible
