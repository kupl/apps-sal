class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = Counter(chars)
        return sum([len(word) for word in words if len(char_counter - Counter(word)) > 1 and len(Counter(word) - char_counter) == 0])
