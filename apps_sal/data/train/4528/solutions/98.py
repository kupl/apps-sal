def my_languages(results):
    g = results.items()
    g = list(g)
    f = []
    g.sort(key=lambda i: i[1])
    for i in g:
        if i[1] >= 60:
            i = f.append(i[0])
    h = f.reverse()
    return f
