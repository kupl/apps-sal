trans = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}


def correct_polish_letters(st):
    empty = []
    for char in st:
        if char not in trans:
            empty.append(char)
        elif char in trans:
            empty.append(trans[char])
    return ''.join(empty)
