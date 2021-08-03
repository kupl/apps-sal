class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if len(mat) == 0:
            return 0
        hist = [0] * len(mat[0])
        res = 0
        for row in mat:
            stack = []
            count = 0
            for i in range(len(row)):
                if row[i]:
                    hist[i] += row[i]
                else:
                    hist[i] = 0

                while stack and hist[stack[-1]] > hist[i]:
                    jj = stack.pop()
                    kk = stack[-1] if stack else -1
                    count -= (hist[jj] - hist[i]) * (jj - kk)

                count += hist[i]
                res += count
                stack.append(i)

        return res
