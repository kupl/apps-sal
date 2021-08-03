def my_languages(results):
    return [i for i in sorted(results, reverse=True, key=results.get) if results[i] >= 60]
