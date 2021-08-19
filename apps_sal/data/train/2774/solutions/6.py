def is_balanced(s, caps):
    s = ''.join((i for i in s if i in caps))
    caps = [caps[i:i + 2] for i in range(0, len(caps), 2)]
    prev = ''
    while s != prev:
        prev = s
        for c in caps:
            s = s.replace(c, '')
    return not s
