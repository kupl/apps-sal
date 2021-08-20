from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        ret = 0
        for word in words:
            if Counter(word) - c == Counter():
                ret += len(word)
        return ret
