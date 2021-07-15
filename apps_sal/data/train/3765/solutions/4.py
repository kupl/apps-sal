def highest_age(group1,group2):
    d = {}
    lst = []
    for i in group1 + group2:
        name = i['name']
        if name in d:
            d[i['name']] += i['age']
        else:
            d[name] = i['age']
    n = max(d.values())
    for k, v in d.items():
        if n == v:
            lst.append(k)
    return min(lst)
