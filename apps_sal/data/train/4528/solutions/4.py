def my_languages(results):
    return sorted([ e for e in results.keys() if results[e]>=60], reverse=True, key=lambda x: results[x])
