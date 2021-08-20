class Solution:

    def beautifulArray(self, N: int) -> List[int]:
        r = [1]
        while len(r) < N:
            o = [2 * i - 1 for i in r]
            e = [2 * i for i in r]
            r = o + e
        ans = []
        for i in range(len(r)):
            if r[i] <= N:
                ans.append(r[i])
        return ans
