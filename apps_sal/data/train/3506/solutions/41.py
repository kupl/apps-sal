def vowel_indices(word):
    index = 1
    res = []
    for i in word.lower():
        if i in "aeiouy":
            res.append(index)
        index += 1
    return res
