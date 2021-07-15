class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(word) for word in words if collections.Counter(word)&collections.Counter(chars)==collections.Counter(word))
