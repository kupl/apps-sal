class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def count(s):
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            return cnt
        cnt = [0] * 26
        for b in B:
            bcnt = count(b)
            for (i, c) in enumerate(bcnt):
                cnt[i] = max(cnt[i], c)
        ans = []
        for a in A:
            acnt = count(a)
            if all((x >= y for (x, y) in zip(acnt, cnt))):
                ans.append(a)
        return ans
