def my_languages(results):
    x = [k for (k, v) in results.items() if v >= 60]
    return sorted(x, key=lambda y: results[y], reverse=True)
