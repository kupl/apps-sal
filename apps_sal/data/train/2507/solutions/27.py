from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = Counter(chars)
        ans = 0
        for word in words:
            cur = Counter(word)
            if cur == cur & d:
                ans += len(word)
        return ans
