def my_languages(results):
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
    return [key for key, value in results.items() if value >= 60][::-1]
