class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter as cnt
        return sum([not cnt(word) - cnt(chars) and len(word) for word in words])
