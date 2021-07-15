class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        def pom(tab):
            stack = []
            sums = [0] * len(tab)
            for i in range(len(tab)):
                while len(stack) > 0 and tab[stack[-1]] > tab[i]:
                    stack.pop()
                if len(stack) == 0:
                    sums[i] = (i + 1) * tab[i]
                else:
                    sums[i] = sums[stack[-1]] + tab[i] * (i - stack[-1])
                stack.append(i)

            return sum(sums)
        
        n_rows = len(mat)
        n_cols = len(mat[0])
        h = [0] * n_cols
        res = 0
        for row in mat:
            for i in range(len(row)):
                if row[i] == 1:
                    h[i] += 1
                else:
                    h[i] = 0
            res += pom(h)
        
        return res
