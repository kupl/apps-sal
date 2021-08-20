def my_languages(results):
    return sorted({k: v for (k, v) in list(results.items()) if v >= 60}, key={k: v for (k, v) in list(results.items()) if v >= 60}.get, reverse=True)
