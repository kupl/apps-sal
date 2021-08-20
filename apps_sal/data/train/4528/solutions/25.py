def my_languages(r):
    return sorted([i for i in r.keys() if r[i] >= 60], key=lambda c: r[c], reverse=True)
