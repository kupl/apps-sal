class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        matrix = [ [str(elem) for elem in row] for row in matrix]
        int_rep_of_matrix = [int(''.join(row),2) for row in matrix]
        
        list_of_k = list(int_rep_of_matrix)
        all_ones = 2**(n)-1
        for elem in int_rep_of_matrix:
            list_of_k.append(elem^all_ones)
        
        answer = 0
        for k in list_of_k:
            current_answer = 0
            for matrix_row in int_rep_of_matrix:
                if matrix_row^k == 0 or  matrix_row^k==all_ones:
                    current_answer += 1
            answer = max(answer,current_answer)
        return answer
                    
                
        

