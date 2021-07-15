def vowel_indices(word):
    ans = []
    c = 1
    for i in [char for char in word.lower()]:
        if i in 'aeiouy':
            ans.append(c)
        c += 1
    return ans
