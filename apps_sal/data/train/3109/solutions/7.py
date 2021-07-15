def scramble_words(words):
    sort = lambda x: x if len(x)<3 else x[0]+''.join(sorted(x[1:-1]))+x[-1]
    find = lambda x : [(i,y) for (i,y) in enumerate(x) if y in ".,'-"]
    mx = []
    for x in words.split():
        l, f = list(''.join(sort([y for y in x if y not in ".,'-"]))), find(x)
        if f:
            l.insert(f[0][0], f[0][1])
        if len(f) == 2:
            l.insert(f[1][0], f[1][1])
        mx.append(''.join(l))
    return ' '.join(mx) if mx else '' 
