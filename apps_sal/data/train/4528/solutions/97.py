def my_languages(results):
    d = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
    return [lang for (lang, mark) in d.items() if mark >= 60]
