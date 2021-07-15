def my_languages(results):
    languages = []
    for language in sorted(results, key=results.get, reverse=True):
        if results[language] > 59:
            languages.append(language)
    return languages
