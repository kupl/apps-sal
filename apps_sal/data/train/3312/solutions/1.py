def anagram_counter(words):
    def is_anagrams(s1, s2): return sorted(s1) == sorted(s2)
    return 0 if not words else sum([1 for x in range(len(words)-1) for y in range(x+1, len(words)) if is_anagrams(words[x], words[y])])
