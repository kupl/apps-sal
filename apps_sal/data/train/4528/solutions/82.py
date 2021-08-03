def my_languages(results):
    list = []
    for x, v in dict(sorted(results.items(), key=lambda x: x[1], reverse=True)).items():
        if v >= 60:
            list.append(x)
    return list
