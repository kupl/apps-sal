def dist(a, b):
    return abs(b[1] - a[1]) + abs(b[0] - a[0])


def pos(a):
    if a in '123456789':
        return [(int(a) - 1) % 3 + 5, (int(a) - 1) // 3]
    d = {'.': [5, 3], '@': [6, 3], '0': [7, 3], 'z': [5, 4], '_': [6, 4], '/': [7, 4]}
    if a in list(d.keys()):
        return d[a]
    return [(ord(a) - 97) % 5, (ord(a) - 97) // 5]


def tv_remote(word):
    word = 'a' + word
    res = 0
    for i in range(len(word) - 1):
        print((word[i], pos(word[i]), word[i + 1], pos(word[i + 1])))
        res += dist(pos(word[i]), pos(word[i + 1]))
    return res + len(word) - 1
