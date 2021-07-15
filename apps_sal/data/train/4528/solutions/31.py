def my_languages(results):
    return sorted([x for x in results if results.get(x)>=60], key = results.get, reverse=True)
