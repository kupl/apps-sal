def encrypt(text, key):
    r = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    km = [[a.index(key[0]), a.index(key[1])], [a.index(key[2]), a.index(key[3])]]
    text = ''.join(x for x in text.lower() if x in a)
    if len(text) % 2:
        text += 'z'
    for i in range(0, len(text), 2):
        tm = [a.index(text.lower()[i]), a.index(text.lower()[i + 1])]
        r += a.upper()[(km[0][0] * tm[0] + km[0][1] * tm[1]) % 26] + a.upper()[(km[1][0] * tm[0] + km[1][1] * tm[1]) % 26]
    return r
