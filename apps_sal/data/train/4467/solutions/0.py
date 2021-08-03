def remember(str_):
    seen = set()
    res = []
    for i in str_:
        res.append(i) if i in seen and i not in res else seen.add(i)
    return res
