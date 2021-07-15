class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        hashmap = {}
        for i in range(m):
            order = \"\"
            first = matrix[i][0]
            
            for j in range(1, n):
                if matrix[i][j] == first:
                    order += \"1\"
                
                else:
                    order += \"0\"
            
            hashmap[order] = hashmap.get(order, 0) + 1
        
        return max(hashmap.values())
