def anagrams(word: str, words: list) -> list: return list(filter(lambda x: sorted(x) == sorted(word), words))
