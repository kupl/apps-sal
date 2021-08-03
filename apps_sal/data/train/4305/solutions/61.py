def order_weight(st):
    res, l = [], st.split(' ')
    d = {x: sum(map(int, list(l[x]))) for x in range(len(l))}
    print(d)
    for x in sorted(set(d.values())):
        res.extend(sorted([l[i] for i in d.keys() if d[i] == x]))
    return ' '.join(res)
