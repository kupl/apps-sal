def anagrams(word, words):
    wordnum = sum(ord(ch) for ch in word)
    res = []
    if not words:
        return []
    for item in words:
        if sum(ord(ch) for ch in item) == wordnum:
            res.append(item)
    return res
