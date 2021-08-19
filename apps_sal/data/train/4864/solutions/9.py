def f(w):
    (l, r) = (0, 0)
    word = ''
    length = len(w)
    n = 0
    while n != length:
        if w[n] == '!':
            if not word:
                l += 1
            else:
                r += 1
        elif w[n].isalpha():
            word += w[n]
        n += 1
    return (l, r, word)


def remove(s):
    l = []
    for x in s.split():
        (a, b, word) = f(x)
        size = min(a, b)
        l.append(f"{'!' * size}{word}{'!' * size}")
    return ' '.join(l)
