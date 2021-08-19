def my_languages(a):
    a = sorted(list(([k, v] for (k, v) in a.items())), key=lambda x: x[1], reverse=True)
    a = list((x[0] for x in a if x[1] >= 60))
    return a
