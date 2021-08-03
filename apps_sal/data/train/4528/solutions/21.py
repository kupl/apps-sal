def my_languages(results):

    return [i[0] for i in sorted(results.items(), key=lambda x: x[1], reverse=True) if i[1] >= 60]
