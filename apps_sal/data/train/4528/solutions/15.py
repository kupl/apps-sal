import operator

def my_languages(results):
    aced = []
    results = dict(sorted(results.items(), key=operator.itemgetter(1), reverse=True))
    for language in results:
        if results[language] >= 60:
            aced.append(language)
    return aced
