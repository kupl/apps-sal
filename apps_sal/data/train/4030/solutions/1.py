def radix_tree(*words):
    byFirstChar = {}
    for w in words:
        if w != '':
            l = byFirstChar.get(w[0], [])
            l.append(w[1:])
            byFirstChar[w[0]] = l
    result = {}
    for (c, l) in byFirstChar.items():
        rt = radix_tree(*l)
        if len(rt) == 1 and (not '' in l):
            for (key, value) in rt.items():
                c = c + key
                rt = value
        result[c] = rt
    return result
