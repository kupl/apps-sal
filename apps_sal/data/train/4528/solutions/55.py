def my_languages(results):
    return sorted([k for k,v in results.items() if v>=60], key=lambda x: 0-results[x])
