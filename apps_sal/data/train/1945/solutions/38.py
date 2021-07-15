class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = collections.defaultdict(int)
        
        for row in matrix:
            if row[0] == 1:
                row = [1 - num for num in row]
            counter[tuple(row)] += 1
        
        return max(counter.values())

