class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        out = 0
        for word in words:
            curr = Counter(word)
            if not curr - count:
                out += len(word)
        return out
