def my_languages(results):
    results = [(x,y) for x,y in results.items() if y >= 60]
    return [i[0] for i in sorted(results, key=lambda x: x[1], reverse = True)]
