def my_languages(results):
    items = []
    list_result = list(results.items())
    list_result.sort(key=lambda i: i[1], reverse=True)
    return [i[0] for i in list_result if i[1] >= 60]
