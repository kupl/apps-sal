def my_languages(results):
    l = []
    for lang in sorted(results, key=results.get, reverse=True):
        if results.get(lang) >= 60:
            l.append(lang)
    return(l)
