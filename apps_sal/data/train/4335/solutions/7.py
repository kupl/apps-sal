from collections import Counter
def anagrams(word, words):
    main = Counter(word)
    return [wor for wor in words if Counter(wor) == main]
