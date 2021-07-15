def my_languages(results):
    results = (r for r in results.items() if r[1] >= 60)
    results = sorted(results, key=lambda r: r[1], reverse=True)
    return [r[0] for r in results]
