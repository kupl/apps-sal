def my_languages(results):
    return [el[0] for el in sorted(results.items(), key=lambda x: x[1], reverse=True) if results[el[0]] >= 60]
