def my_languages(results):
    results = sorted(list(results.items()), key=lambda x: x[1], reverse=True)
    return [i[0] for i in results if i[1]>=60]

