def brainfuck_to_c(s):
    s = ''.join([x for x in s if x in '+-><[].,'])
    rep = ['+-', '-+', '<>', '><', '[]']
    while sum([s.count(x) for x in rep]):
        for i in rep:
            s = s.replace(i, '')
    if len(s) == 0:
        return ''
    (t, r, shift) = ([s[0]], '', 0)
    for i in range(1, len(s)):
        if s[i] in t[-1] and s[i] in '+-<>':
            t[-1] += s[i]
        else:
            t += [s[i]]
    for i in t:
        if '+' in i:
            r += ' ' * 2 * shift + '*p += ' + str(len(i)) + ';\n'
        if '>' in i:
            r += ' ' * 2 * shift + 'p += ' + str(len(i)) + ';\n'
        if '-' in i:
            r += ' ' * 2 * shift + '*p -= ' + str(len(i)) + ';\n'
        if '<' in i:
            r += ' ' * 2 * shift + 'p -= ' + str(len(i)) + ';\n'
        if i == '.':
            r += ' ' * 2 * shift + 'putchar(*p);\n'
        if i == ',':
            r += ' ' * 2 * shift + '*p = getchar();\n'
        if i == ']':
            shift -= 1
            if shift < 0:
                return 'Error!'
            r += ' ' * 2 * shift + '} while (*p);\n'
        if i == '[':
            r += ' ' * 2 * shift + 'if (*p) do {\n'
            shift += 1
    return 'Error!' if shift > 0 else r
