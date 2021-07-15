def anagrams(word, words):
    return [el for el in words if sorted(word) == sorted(el)]
