def my_languages(results):
    res_sorted = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in res_sorted if x[1] >= 60]
