def my_languages(results):
    return list(map(lambda x: x[0], sorted([(x, results[x]) for x in results if results[x] >= 60], key=lambda x: x[1], reverse=True)))
