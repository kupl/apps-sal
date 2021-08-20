def my_languages(results):
    result = []
    sort_orders = sorted(results.items(), key=lambda x: x[1], reverse=True)
    for (key, value) in sort_orders:
        if value >= 60:
            result.append(key)
    return result
