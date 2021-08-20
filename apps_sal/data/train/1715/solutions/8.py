def justify(txt, wid):
    (result, i, j, n) = ([], 0, 0, txt.find(' '))
    while True:
        while -1 < n and n - i <= wid:
            (j, n) = (n, txt.find(' ', n + 1))
        if n < 0 and len(txt[i:]) <= wid:
            result.append(txt[i:])
            break
        result.append(expand(txt[i:j], wid))
        i = j + 1
    return '\n'.join(result)


def expand(line, wid):
    (gap, spc, f) = (wid - len(line), line.count(' '), ' '.center)
    (b, r) = divmod(gap, spc) if spc else (0, 0)
    return line.replace(' ', f(b + 1)).replace(f(b + 1), f(b + 2), r)
