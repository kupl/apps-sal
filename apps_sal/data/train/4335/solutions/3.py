def anagrams(word, words):
    return [w for w in words if sorted(word)==sorted(w)]
