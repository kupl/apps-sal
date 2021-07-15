class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        all_1 = [1] * m
        
        dic = {}
        for li in matrix:
            if li[0] == 0:
                li = [1 if i == 0 else 0 for i in li]
            s = ''.join([str(i) for i in li])
            if s in dic:
                dic[s] +=1
            else:
                dic[s] = 1
                
        return max(dic.values())
        
        

