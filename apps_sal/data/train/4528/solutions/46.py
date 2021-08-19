def my_languages(results):
    return sorted((j for (j, k) in results.items() if k >= 60), reverse=True, key=results.get)
