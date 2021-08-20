class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        (N, M) = (len(mat), len(mat[0]))
        for i in range(N):
            mask = mat[i]
            for j in range(i, N):
                if j > i:
                    mask = [int(i & j) for (i, j) in zip(mask, mat[j])]
                cnt = 0
                for k in mask:
                    if k == 1:
                        cnt += 1
                    else:
                        ans += cnt * (cnt + 1) // 2
                        cnt = 0
                ans += cnt * (cnt + 1) // 2
        return ans
