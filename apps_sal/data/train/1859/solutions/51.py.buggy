class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def do_dfs(r,c):
            \"\"\"Recursive DFS\"\"\"
            res = float('inf')

            for move in moves:
                cand_row = r + move[0]
                cand_col = c + move[1]

                if check_validity(cand_row, cand_col):
                    res = min(res, do_dfs(cand_row, cand_col))
                else:
                    res = 0
            res += 1 #The square itself is a one-sided sq because it is 1
            total_squares[0] += res
            print (r,c, res)
            return res
        
        def check_validity(r,c):
            \"\"\"Check if r,c is in-bounds and equal to 1 \"\"\"

            if 0<=r<R and 0<=c<C and matrix[r][c]==1 :
                return True

            return False

        total_squares = [0]

        if not matrix:
            return total_squares[0]

        moves = ((0,1),(1,1),(1,0))

        R,C = len(matrix), len(matrix[0])

        for r in range(R):
            for c in range(C):
                if check_validity(r,c):
                    do_dfs(r,c)

        return total_squares[0]

