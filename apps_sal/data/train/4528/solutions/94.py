def my_languages(results):
    y = []
    for key, value in sorted(results.items(), key=lambda x: x[1], reverse=True):
        if value >= 60:
            y.append(key)
    return y
