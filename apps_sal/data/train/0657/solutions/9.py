class Solution:

    def matrixScore(self, A):
        (m, n) = (len(A), len(A[0]))
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] ^= 1
        for j in range(n):
            cnt = sum((A[i][j] for i in range(m)))
            if cnt < m - cnt:
                for i in range(m):
                    A[i][j] ^= 1
        return sum((int(''.join(map(str, A[i])), 2) for i in range(m)))


(n, m) = map(int, input().split())
A = []
for _ in range(n):
    x = list(map(int, input().split()))
    A.append(x)
c = Solution()
print(c.matrixScore(A))
