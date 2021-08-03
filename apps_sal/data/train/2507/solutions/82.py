class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        return sum(len(word) for word in words if not (Counter(word) - chars))
