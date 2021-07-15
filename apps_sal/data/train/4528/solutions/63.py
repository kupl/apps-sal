def my_languages(results):
    lst = [x for x in results if results.get(x) >= 60]
    return sorted(lst, key=lambda x: results.get(x), reverse=True)
