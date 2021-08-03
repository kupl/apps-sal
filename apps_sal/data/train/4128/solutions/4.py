def bears(x, s):
    k = []
    i = 0
    while i < len(s) - 1:
        if s[i] == 'B' and s[i + 1] == '8' or s[i] == '8' and s[i + 1] == 'B':
            k.append(s[i] + s[i + 1])
            i += 2

        else:
            i += 1
    return [''.join(k), len(k) >= x] if k else ['', len(k) >= x]
