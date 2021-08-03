def anagrams(word, words): return list(w for w in words if sorted(list(w)) == sorted(list(word)))
