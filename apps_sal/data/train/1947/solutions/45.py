class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = [0] * 26
        for b in B:
            cnt1 = [0] * 26
            for c in b:
                cnt1[ord(c) - 97] += 1
            for (i, j) in enumerate(cnt1):
                cnt[i] = max(cnt[i], j)
        result = []
        for a in A:
            cnt1 = [0] * 26
            for c in a:
                cnt1[ord(c) - 97] += 1
            if all((j <= cnt1[i] for (i, j) in enumerate(cnt))):
                result.append(a)
        return result
