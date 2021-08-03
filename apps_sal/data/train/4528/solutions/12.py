def my_languages(results):
    return sorted([k for k in results if results[k] >= 60], key=lambda x: results[x], reverse=True)
