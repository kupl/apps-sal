def triangle(s):
    n = len(s)
    out = []
    if n == 1:
        return s
    else:
        for i in range(n - 1):
            f = ['R', 'G', 'B']
            if s[i] == s[i + 1]:
                out.append(s[i])
            else:
                f.remove(str(s[i]))
                f.remove(str(s[i + 1]))
                out.extend(f)
        s = ''.join(out)
    if len(s) == 1:
        return s
    else:
        return triangle(s)
