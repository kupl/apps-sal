from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        if len(B) == 0:
            return []
        ans = []
        ca = [Counter(a) for a in A]
        cb = Counter(B[0])
        for i in range(1, len(B)):
            lb = Counter(B[i])
            for c in lb:
                cb[c] = max(cb[c], lb[c])
        for i in range(len(A)):
            isUniv = True
            if len(cb - ca[i]) > 0:
                continue
            ans.append(A[i])
        return ans
