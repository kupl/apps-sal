letter_corr = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}


def correct_polish_letters(st):
    l = []
    for i in st:
        l.append(letter_corr.get(i, i))
    return ''.join(l)
