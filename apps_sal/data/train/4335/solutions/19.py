anagrams=lambda word, words:list(w for w in words if sorted(list(w))==sorted(list(word)))
