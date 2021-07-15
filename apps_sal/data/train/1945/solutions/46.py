from collections import Counter
class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        counter = Counter()
        flip = {1: 0, 0: 1}
        
        for row in matrix:
            if row[0] == 0 :
                row = [flip[col] for col in row]
                
            counter[tuple(row)] += 1
            
        return max(counter.values())
