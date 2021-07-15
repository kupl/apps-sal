class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(not Counter(w) - Counter(chars) and len(w) for w in words)
