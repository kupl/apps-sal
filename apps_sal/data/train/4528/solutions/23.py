def my_languages(results):
    results = sorted(results.items(), key=lambda d: d[1], reverse=True)
    res = []
    for item in results:
        if item[1] >= 60:
            res.append(item[0])
    return res
