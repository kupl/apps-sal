def my_languages(d):
    l = {}
    res = []
    s = d.items()
    for i in s:
        l[i[1]] = i[0]
    s = sorted(l, reverse=True)
    res = [l[i] for i in s if i >= 60]
    return res
