def atomic_number(electrons):
    (level, shells) = (1, [])
    while electrons:
        shells.append(min(2 * level * level, electrons))
        (electrons, level) = (electrons - shells[-1], level + 1)
    return shells
