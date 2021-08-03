def string_constructing(a, b):
    s, c = [], 0
    while ''.join(s) != b:
        s.extend(list(a))
        c += 1
        i = 0
        while i < len(s) and i < len(b):
            if s[i] == b[i]:
                i += 1
            else:
                c += 1
                s.pop(i)
        if ''.join(s).startswith(b):
            c += len(s[len(b):])
            break
    return c
