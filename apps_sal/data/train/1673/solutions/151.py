class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr[0])
        table = [arr[0][i] for i in range(m)]
        
        def get_mins(table):
            cur_min = int(1e+9)
            cur_min_i = -1
            next_cur_min = int(1e+9)
            next_cur_min_i = -1
            for i, x in enumerate(table):
                if x <= cur_min:
                    cur_min, cur_min_i = x, i
            for i, x in enumerate(table):
                if x <= next_cur_min and i != cur_min_i:
                    next_cur_min, next_cur_min_i = x, i
            return cur_min, cur_min_i, next_cur_min, next_cur_min_i 
        
        cur_min, cur_min_i, next_cur_min, next_cur_min_i = get_mins(table)
        for i in range(1, len(arr)):
            for j in range(m):
                table[j] = arr[i][j]
                if j != cur_min_i:
                    table[j] = arr[i][j] + cur_min
                else:
                    table[j] = arr[i][j] + next_cur_min
            cur_min, cur_min_i, next_cur_min, next_cur_min_i = get_mins(table)
        return cur_min

