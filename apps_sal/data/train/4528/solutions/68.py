def my_languages(results):
    arr = sorted([x for x in results.values() if x >= 60 ])
    rev_res = {}
    for key in results:
        rev_res[results[key]] = key
    return [rev_res[x] for x in arr[::-1]]
