
def my_languages(results):
    dgu = sorted(list(results.items()), key=lambda x: x[1], reverse=True)
    a = []
    for i in dgu:
        li = list(i)
        if li[1] >= 60:
            for u in li:
                if isinstance(u, str):
                    a.append(u)
    return a
