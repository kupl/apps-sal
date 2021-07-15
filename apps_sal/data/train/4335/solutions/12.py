def anagrams(word, words):
    return [x for x in words if sorted(word) == sorted(x)]
