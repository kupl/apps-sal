def pair_of_shoes(shoes):
    return not sum((size * (-1)**side) for side, size in shoes)
