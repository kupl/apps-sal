from itertools import product


def child(bird1, bird2):
    return sum([b[0] != b[1] for b in zip(bird1, bird2)]) in (1, 2)


def grandchild(bird1, bird2):
    for mother in product("BW", repeat=len(bird1)):
        if child(bird1, mother) and child(bird2, mother):
            return True
    return False
