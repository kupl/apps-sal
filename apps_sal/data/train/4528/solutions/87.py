def my_languages(r):
    return [x for x in sorted(r, key=lambda x:r[x], reverse=True) if r[x] >= 60]
