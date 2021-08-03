def super_pad(s, w, f=" "):
    if not f:
        return s
    if not w:
        return ""
    if f[0] == '>':
        return (s + f[1:] * w)[:w]
    if f[0] == '^':
        l = r = (f[1:] * w)[:(w - len(s)) // 2 + (1 if (w - len(s)) & 1 else 0)]
        return (l + s + r)[:w]
    return (((f[1:] if f[0] == '<' else f) * w)[:w - len(s)] + s)[-w:]
