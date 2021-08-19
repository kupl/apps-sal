def diffs(bird1, bird2):
    return sum((c1 != c2 for (c1, c2) in zip(bird1, bird2)))


def child(bird1, bird2):
    return diffs(bird1, bird2) in [1, 2]


def grandchild(bird1, bird2):
    return diffs(bird1, bird2) in [0, 1, 2, 3, 4] if len(bird1) > 1 else bird1 == bird2
