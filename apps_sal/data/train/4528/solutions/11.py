def my_languages(d):
    return sorted((x for (x, y) in d.items() if y >= 60), key=lambda x: -d[x])
