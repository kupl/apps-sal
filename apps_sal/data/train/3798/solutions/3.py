def cards_and_pero(s):
    d, records = {'P': 13, 'K': 13, 'H': 13, 'T': 13}, []
    for i in range(0, len(s), 3):
        t = s[i:i + 3]
        if t in records:
            return [-1] * 4
        records.append(t)
        d[t[0]] -= 1
    return list(d.values())
