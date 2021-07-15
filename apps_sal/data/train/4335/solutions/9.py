def anagrams(word, words):
    return [w for w in words if list(sorted(w)) == list(sorted(word))]
