from collections import Counter as di


class Solution:

    def countCharacters(self, a: List[str], c: str) -> int:
        d = di(c)
        ans = 0
        for i in a:
            d1 = di(i)
            if len(d1 - d) == 0:
                ans += sum(d1.values())
        return ans
