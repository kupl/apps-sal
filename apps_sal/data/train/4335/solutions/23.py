from collections import Counter
def anagrams(word, words):
    # your code here
    return [w for w in words if sorted(sorted(Counter(word).items())) == sorted(sorted(Counter(w).items()))]
