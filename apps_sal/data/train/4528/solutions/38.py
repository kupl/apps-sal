def my_languages(results):
    return [n for n in sorted(results, key=results.get, reverse=True) if results.get(n) >= 60]
