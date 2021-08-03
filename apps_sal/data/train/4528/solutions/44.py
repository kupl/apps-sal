def my_languages(results):
    temp = [k for k, v in sorted(list(results.items()), key=lambda x:x[1], reverse=True) if results[k] >= 60]
    return temp
