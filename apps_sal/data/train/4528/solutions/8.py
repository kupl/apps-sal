def my_languages(results):
    return sorted([lang for lang in results if results[lang] >= 60], key=lambda l: -results[l])
