def change_case(id, t):
    q = ('_' in id) + ('-' in id) + any(x.isupper() for x in set(id))
    if q > 1: return
    d = {'kebab': '-', 'snake': '_'}
    l, index = [''], 0
    for x in id:
        if not l[index] or not x.isupper() and x.isalpha() and l[index][-1].isalpha():
            l[index] += x
        elif x.isalpha():
            l.append(x)
            index += 1
        else:
            l.append('')
            index += 1

    if t in d:
        return f'{d[t]}'.join(x.lower() for x in l)
    if t == 'camel':
        return ''.join(w.capitalize() if i else w for i,w in enumerate(l))
