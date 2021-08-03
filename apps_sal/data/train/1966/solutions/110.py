from collections import defaultdict


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        n, m = len(mat), len(mat[0])
        cnt = 0

        def count(arr):
            cnt = [0] * len(arr)
            if arr[0] == 1:
                cnt[0] = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] == 1:
                    cnt[i] = cnt[i - 1] + 1
                elif arr[i] == 1:
                    cnt[i] = 1
                else:
                    cnt[i] = 0
            return sum(cnt)

        ans = 0

        for left in range(m):
            c = [1 for i in range(n)]
            for right in range(left, m):
                for i in range(n):
                    c[i] = c[i] and mat[i][right]
                ans += count(c)

        return ans
