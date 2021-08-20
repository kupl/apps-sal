def my_languages(results):
    dictCopy = results.copy()
    for (k, v) in dictCopy.items():
        if v < 60:
            del results[k]
    results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    languages = []
    for i in range(len(results)):
        languages.append(results[i][0])
    return languages
