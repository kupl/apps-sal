def my_languages(results):
    return sorted([r for r in results if results[r] >= 60], key=results.get, reverse=True)
