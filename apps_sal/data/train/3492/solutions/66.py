def correct_polish_letters(st):
    (s, p, n) = ('', ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż'], ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z'])
    for i in list(st):
        if i in p:
            s += n[p.index(i)]
        else:
            s += i
    return s
