class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
                return sum( len(w) for w in words if not Counter(w) - Counter(chars))

