def my_languages(results):
    return [k for k, v in sorted(list(results.items()), key=lambda kv: -kv[1]) if v >= 60]

