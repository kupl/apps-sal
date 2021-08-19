def child(b1, b2):
    return 0 < sum([i != j for (i, j) in zip(b1, b2)]) < 3


def grandchild(b1, b2):
    return sum([i != j for (i, j) in zip(b1, b2)]) < 5 and b1 + b2 not in ['WB', 'BW']
