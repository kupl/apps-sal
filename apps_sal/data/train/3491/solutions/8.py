def substring(s):
    r = []
    for (i, x) in enumerate(s):
        temp = [x]
        for j in range(i + 1, len(s)):
            if s[j] in temp or len(set(temp)) < 2:
                temp.append(s[j])
            else:
                r.append(''.join(temp))
                break
        r.append(''.join(temp))
    return s and max(r, key=len) or ''
