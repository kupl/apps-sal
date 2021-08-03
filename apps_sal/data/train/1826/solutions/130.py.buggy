import copy
class Solution:    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n_row = len(mat)
        n_column = len(mat[0])        
        
        print(n_row, n_column, K , \"n_row, n_column, K\")
        
        memo = [[0 for _ in range(n_column)] for _ in range(n_row)]
        new_mat = [[0 for _ in range(n_column)] for _ in range(n_row)]
        
        ## column wise memoization    
        if n_row > n_column:        
            for i in range(n_row):
                for j in range(n_column):                    
                    start_row= 0 if i-K <0 else i-K
                    end_row = n_row-1 if i+K > n_row-1 else i+K
                    
                    for r in range(start_row, end_row+1):
                        memo[i][j] +=mat[r][j]                        
        else:
            for i in range(n_row):
                for j in range(n_column):                    
                    start_column= 0 if j-K <0 else j-K
                    end_column = n_column-1 if j+K > n_column-1 else j+K
                    
                    for r in range(start_column, end_column+1):
                        memo[i][j] +=mat[i][r]                                            
                    
        print(len(memo), len(memo[0]), \"n_row , n_columns of memo\")
                        
        ## main calculation
        if n_row > n_column:
            for i in range(n_row):
                for j in range(n_column):    
                    start_column= 0 if j-K <0 else j-K
                    end_column = n_column-1 if j+K > n_column-1 else j+K                    
                    
                    for r in range(start_column, end_column+1):
                        new_mat[i][j] += memo[i][r] 
        else:
            for i in range(n_row):
                for j in range(n_column):
                    start_row= 0 if i-K <0 else i-K
                    end_row = n_row-1 if i+K > n_row-1 else i+K
                    
                    for r in range(start_row, end_row+1):
                        new_mat[i][j] += memo[r][j] 
                    
        return new_mat
