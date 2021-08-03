def my_languages(results):
    return [x for x, value in sorted(results.items(), key=lambda item: -item[1]) if value >= 60]
