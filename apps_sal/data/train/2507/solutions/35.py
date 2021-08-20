from collections import Counter


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        c1 = Counter(chars)
        ans = 0
        for i in words:
            c2 = Counter(i)
            print(c2 - c1)
            if not c2 - c1:
                ans += len(i)
        return ans
