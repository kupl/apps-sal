\"\"\"
用increasing monostack找到以(i, j)结尾的全为1的最大rectangle, 就很容易计算以(i, j)结尾submatrices的个数了.
\"\"\"
class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]  # construct the histogram 
                
        res = 0
        for i in range(m):
            res += self._histogram(matrix[i])       # helper function return the total cnt of row i
        return res
        
    def _histogram(self, heights):
        \"\"\"
        算法核心是：以j结尾的submatrices的个数等于heights[j] * (j - 向左找第一个height小于heights[j]的idx)
        算法是84.Largest-Rectangle-in-Histogram, 85.Maximal-Rectangle. we need maintain an increasing stack
        \"\"\"
        cnt = [0 for _ in range(len(heights))]
        st = []
        for j, height in enumerate(heights):
            while len(st) > 0 and st[-1][0] >= height:
                st.pop()
                
            if len(st) == 0:
                cnt[j] = height * (j + 1)
            else:
                cnt[j] = height * (j - st[-1][1]) + cnt[st[-1][1]]
                
            st.append((height, j))

        return sum(cnt)
