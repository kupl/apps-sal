class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        ans = 0
        chars_set = set(chars)
        count0 = Counter(chars)
        for word in words:
            count = Counter(word)
            if all((s in chars_set and count[s] <= count0[s] for s in word)):
                ans += len(word)
        return ans
