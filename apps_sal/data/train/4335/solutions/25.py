def anagrams(word, words):
    return [anagram for anagram in words if sum([ord(c) for c in anagram]) == sum([ord(c) for c in word])]

