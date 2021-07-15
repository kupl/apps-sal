def my_languages(results):
    d = sorted([(v,k) for k,v in results.items()], reverse=True)
    return [i[1] for i in d if i[0] >= 60]
