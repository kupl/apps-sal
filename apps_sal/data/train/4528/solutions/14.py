def my_languages(results):
    s = [(k, results[k]) for k in sorted(results, key=results.get, reverse=True)]
    return [i[0] for i in s if i[1]>=60]
