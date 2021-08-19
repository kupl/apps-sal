def my_languages(r):
    return [k for (k, v) in sorted(r.items(), key=lambda i: i[1]) if v >= 60][::-1]
