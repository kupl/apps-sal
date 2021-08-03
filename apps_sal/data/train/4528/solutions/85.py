def my_languages(results):
    for x, y in list(results.items()):
        if y < 60:
            del results[x]
    results = sorted(results, key=results.get, reverse=True)
    return results
