def my_languages(results):
    results = {lang: results[lang] for lang in results if results[lang] >= 60}
    results = sorted(results, key=results.get)
    results.reverse()
    return results
