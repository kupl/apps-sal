def my_languages(results):
    to_return = []
    for i in range(100, 59, -1):
        for key, value in results.items():
            if (value >= i) and not (key in to_return):
                to_return.append(key)
    return to_return
