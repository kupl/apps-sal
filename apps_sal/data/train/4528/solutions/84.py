def my_languages(results):
    for x, y in list(results.items()):
        if y < 60:
            del results[x]
    return sorted(results, key=results.get, reverse=True)
