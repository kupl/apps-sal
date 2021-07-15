def my_languages(results):
    lang = []
    final = []
    for key in results:
        if results[key] > 59:
            if results[key] == 100:
                results[key] = 99
            lang.append(str(results[key]) + key)
    lang.sort(reverse=True)
    for word in lang:
        final.append(word[2:len(word)])
    return final
