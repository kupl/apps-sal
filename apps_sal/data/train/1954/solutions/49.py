from functools import lru_cache


class Solution:
    def smallestSufficientTeam(self, l1: List[str], l2: List[List[str]]) -> List[int]:

        n = len(l1)
        l2 = [set(i) for i in l2]

        index = {}
        for i in range(n):
            index[l1[i]] = i

        @lru_cache(None)
        def dp(mask, i):
            # if mask == 2 ** n - 1:return set()
            if i == n:
                return set() if mask == 2 ** n - 1 else set(range(len(l2)))

            curr = set(range(len(l2)))

            if (mask >> i) & 1 == 1:
                temp = dp(mask, i + 1)
                if len(temp) < len(curr):
                    curr = temp

            for ind, j in enumerate(l2):
                if l1[i] in j:
                    masknow = mask
                    for k in j:
                        if (masknow >> index[k]) & 1 == 0:
                            masknow += (1 << index[k])
                    temp = set([ind]) | dp(masknow, i + 1)

                    if len(temp) < len(curr):
                        curr = temp
            return curr

        return sorted(list(dp(0, 0)))
