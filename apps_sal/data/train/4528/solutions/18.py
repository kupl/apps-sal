def my_languages(results):
    return [k for (k, v) in sorted(results.items(), key=lambda item: item[1], reverse=True) if v > 59.99]
