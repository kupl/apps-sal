def my_languages(results):
    valid = [k for k in results if results[k] >= 60]
    return sorted(valid, key=lambda x: results[x], reverse=True)
