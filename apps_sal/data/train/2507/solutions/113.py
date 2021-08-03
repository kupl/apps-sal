from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        r = Counter(chars)
        return sum([len(word) if Counter(word) - r == Counter() else 0 for word in words])
