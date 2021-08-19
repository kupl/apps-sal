def correct_polish_letters(st):
    # your code here
    d = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    return ''.join(map(lambda x: x.replace(x, d.get(x, x)), st))
