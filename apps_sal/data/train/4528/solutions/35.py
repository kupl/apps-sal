def my_languages(results):
    results = sorted(results.items(), key=lambda x: x[1],
                    reverse = True) 
    result = []
    for i in results:
        if i[1] >= 60:
            result.append(i[0])
    return result
