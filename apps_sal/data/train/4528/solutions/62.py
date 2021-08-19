def my_languages(results):
    return sorted({key: value for (key, value) in results.items() if value >= 60}, key=results.get, reverse=True)
