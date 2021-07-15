def my_languages(results):
    return sorted(filter(lambda x: results[x] >= 60, results), key = lambda x: results[x], reverse = True)
