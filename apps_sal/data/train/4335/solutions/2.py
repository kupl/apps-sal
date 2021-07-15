def anagrams(word, words):
    match = sorted(word)
    return [w for w in words if match == sorted(w)]
