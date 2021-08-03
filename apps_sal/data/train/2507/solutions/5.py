class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        chars_map = collections.Counter(chars)
        for word in words:
            if collections.Counter(word) == (collections.Counter(word) & chars_map):
                count += len(word)
        return count
