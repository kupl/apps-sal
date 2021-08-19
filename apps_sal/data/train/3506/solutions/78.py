def vowel_indices(word):
    word = word.lower()
    a = ['a', 'e', 'i', 'o', 'u', 'y']
    res = []
    count = 1
    for i in word:
        if i in a:
            res.append(count)
        count += 1
    return res
