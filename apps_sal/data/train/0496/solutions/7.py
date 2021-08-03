from collections import Counter


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        hm = dict(Counter(A))
        stack = [k for k, v in list(hm.items()) if v > 1]
        ans = 0
        while stack:
            k = stack.pop()
            hm[k + 1] = hm.get(k + 1, 0) + hm[k] - 1
            ans += hm[k] - 1
            hm[k] = 1
            if hm[k + 1] > 1:
                stack.append(k + 1)

        return ans
