def anagram_counter(words):
    anagrams = 0
    for i, word in enumerate(words):
        for wrd in [w for w in words if w != word and set(word) == set(w)]:
            anagrams += 1
    return anagrams / 2
