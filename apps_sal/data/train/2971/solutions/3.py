def watch_pyramid_from_the_side(characters):
    if not characters: return characters
    l = len(characters)
    return '\n'.join(' '*(l-i-1) + c*(2*i+1) + ' '*(l-i-1) for i,c in enumerate(characters[::-1]))

def watch_pyramid_from_above(characters):
    if not characters: return characters
    l = len(characters)*2 - 1
    return '\n'.join(''.join(characters[min(i, j, l-i-1, l-j-1)] for j in range(l)) for i in range(l))

def count_visible_characters_of_the_pyramid(characters):
    if not characters: return -1
    return 1 + sum(4*i for i in range(2, 2*len(characters), 2))

def count_all_characters_of_the_pyramid(characters):
    if not characters: return -1
    return sum(i**2 for i in range(1, 2*len(characters), 2))
