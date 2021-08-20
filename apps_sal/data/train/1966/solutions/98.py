class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        ar = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])):
                if mat[i][j]:
                    c += 1
                else:
                    c = 0
                ar[i][j] = c
        for r in mat:
            print(r)
        print()
        for r in ar:
            print(r)
        print()
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                x = float('inf')
                for k in range(i, len(mat)):
                    x = min(x, ar[k][j])
                    ans += x
        return ans
