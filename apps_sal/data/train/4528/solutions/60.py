def my_languages(results):
    sor = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    a = []
    for i in sor:
        if sor[i] >= 60:
            a.append(i)
    return a
