class Solution:

    def numSubmat(self, A: List[List[int]]) -> int:
        (m, n) = (len(A), len(A[0]))
        res = 0
        for i in range(m):
            r = [1] * n
            for j in range(i, m):
                for k in range(n):
                    r[k] &= A[j][k]
                res += self.count(r)
        return res

    def count(self, r):
        res = head = 0
        for n in r:
            head = head + 1 if n else 0
            res += head
        return res
