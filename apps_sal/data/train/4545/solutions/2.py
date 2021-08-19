from cmath import pi, polar
SECTIONS = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
RINGS = [12.7, 31.8, 198, 214, 324, 340]
SCORES = 'DB SB {} T{} {} D{} X'.split()


def get_score(x, y):
    (r, phi) = polar(x + 1j * y)
    (r, phi) = (2 * r, phi + pi / 20)
    section = SECTIONS[int(10 * phi // pi)]
    for (d, f) in zip(RINGS, SCORES):
        if r < d:
            return f.format(section)
    return SCORES[-1]
