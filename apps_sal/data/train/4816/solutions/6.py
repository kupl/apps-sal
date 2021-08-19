def diff(bird1, bird2):
    return sum((c1 != c2 for (c1, c2) in zip(bird1, bird2)))


def child(bird1, bird2):
    return 1 <= diff(bird1, bird2) <= 2


def grandchild(bird1, bird2):
    d = diff(bird1, bird2)
    if len(bird1) == 1:
        return d == 0
    return 0 <= d <= 4
