class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        max_b = [0] * 26
        for i in range(len(B)):
            local_b = [0] * 26
            for c in B[i]:
                local_b[ord(c) - 97] += 1
            for i in range(26):
                max_b[i] = max(max_b[i], local_b[i])
        for i in range(len(A)):
            local_a = [0] * 26
            for c in A[i]:
                local_a[ord(c) - 97] += 1
            for k in range(26):
                if local_a[k] < max_b[k]:
                    break
                if k == 25:
                    res.append(A[i])
        return res
