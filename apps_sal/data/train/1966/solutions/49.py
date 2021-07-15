class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        print(\"rows = {}; cols = {}\".format(rows, cols))
        
        cnt = 0
        
        for tl_row in range(0, rows):
            for tl_col in range(0, cols):
                # May be \"retracted\" as we go along:
                max_width = cols - tl_col
                
                for height in range(1, rows - tl_row + 1):
                    for width in range(1, max_width + 1):
                        cell = mat[tl_row + height - 1][tl_col + width - 1]
                        if cell == 1:
                            cnt += 1
                            continue
                        else:
                            max_width = width - 1
                            break
                            
                    if max_width == 0:
                        break

        return cnt                        
        
