class Solution:
    def get_matrix_cnt(self, cur_row_height):
        res = 0
        for i, polm in enumerate(cur_row_height):
            
            if polm > 0:
                for cur_height in range(1, polm+1):
                    res += 1
                    cur_index = i+1
                    while cur_index < len(cur_row_height) and cur_row_height[cur_index] >= cur_height:
                        res +=1
                        cur_index += 1
        return res
                    
        
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])
        
        cur_row_height = [0] * n
        total = 0
        for row in range(m):
            # get cumulated height based on current row
            for col in range(n):
                if mat[row][col] == 0:
                    cur_row_height[col] = 0
                else:
                    cur_row_height[col] += 1
            
            #print(cur_row_height)
            cur_cnt = self.get_matrix_cnt(cur_row_height)
            total += cur_cnt
            #print(cur_cnt)
        return total
