def watch_pyramid_from_the_side(characters):
    if not characters: return characters
    s = characters[::-1]
    n = len(s) * 2 - 1
    return '\n'.join('{:^{}}'.format(c * i, n) for i, c in zip(range(1, len(s) * 2, 2), s))

def watch_pyramid_from_above(characters):
    if not characters: return characters
    s = characters[::-1]
    n = len(s)
    return '\n'.join(
        ''.join(s[max(abs(i), abs(j))] for j in range(-n+1, n))
        for i in range(-n+1, n)
    )

def count_visible_characters_of_the_pyramid(characters):
    if not characters: return -1
    n = len(characters) * 2 - 1
    return n ** 2

def count_all_characters_of_the_pyramid(characters):
    if not characters: return -1
    return sum(n**2 for n in range(1, 2 * len(characters), 2))
