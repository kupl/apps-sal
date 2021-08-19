def brainfuck_to_c(s):
    s = ''.join((c for c in s if c in '.,<>[]-+'))
    pairs = '<> >< -+ +- []'.split()
    while any((p in s for p in pairs)):
        for w in pairs:
            s = s.replace(w, '')
    (r, depth, l, i) = ('', 0, ' ', 1)
    for c in s:
        if c == l and c in '<>+-':
            i += 1
            continue
        if l in '<>+-':
            r += cmd(depth, l, i)
        if c == ']':
            depth -= 2
        if c in '.,[]':
            r += cmd(depth, c)
        if c == '[':
            depth += 2
        if depth < 0:
            break
        (i, l) = (1, c)
    return 'Error!' if depth else r + (cmd(depth, l, i) if l in '<>+-' else '')


def cmd(depth, c, i=None):
    return ' ' * depth + {'<': 'p -=', '>': 'p +=', '+': '*p +=', '-': '*p -=', '.': 'putchar(*p);', ',': '*p = getchar();', '[': 'if (*p) do {', ']': '} while (*p);'}[c] + (' {};'.format(i) if i else '') + '\n'
