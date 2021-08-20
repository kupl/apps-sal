from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = Counter(chars)
        out = 0
        for word in words:
            length = len(word)
            if not Counter(word) - letters:
                out += length
        return out
