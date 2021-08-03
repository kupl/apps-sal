from functools import reduce


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cntB = [Counter(b) for b in B]
        sumB = reduce(lambda x, y: x | y, cntB)
        ans = []
        for a in A:
            cnt = Counter(a)
            if all(sumB[s] <= cnt[s] for s in sumB):
                ans.append(a)
        return ans
