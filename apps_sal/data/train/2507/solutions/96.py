class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum([len(word) for word in words if len(collections.Counter(word) - collections.Counter(chars)) == 0])
