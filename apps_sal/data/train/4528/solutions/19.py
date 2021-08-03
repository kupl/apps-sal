def my_languages(results):
    # your code here
    return [x for x, y in list(sorted(results.items(), key=lambda x:x[1], reverse=True)) if y >= 60]
