def my_languages(results):

    def myFunc(e):
        return e[1]
    languages = []
    result = []
    for (language, score) in results.items():
        if score >= 60:
            languages.append([language, score])
    languages.sort(key=myFunc, reverse=True)
    for item in languages:
        result.append(item[0])
    return result
