class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        return sum(len(w) for w in words if not Counter(w) - chars)
