import re


def top_3_words(text):
    panctuation = "_'"
    list_word = re.findall("[a-z0-9A-Z\\']+", text.lower())
    result = []
    dict1 = {}
    for word in list_word:
        if word and word != "'" and (word != "'''"):
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
    result = sorted(list(dict1.items()), reverse=True, key=lambda x: x[1])
    result = result[:3] if len(result) > 3 else result
    return [res[0] for res in result]
