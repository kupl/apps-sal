def hamming(a, b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))


def child(bird1, bird2):
    return 1 <= hamming(bird1, bird2) <= 2


def grandchild(bird1, bird2):
    if len(bird1) == 1:
        return bird1 == bird2
    return 0 <= hamming(bird1, bird2) <= 4
