class Solution:
    def flip_row(self, row):
        for i, val in enumerate(row):
            if val == 0:
                row[i] = 1
            else:
                row[i] = 0
        return row
       
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # O(n^2) time, O(n) space
        seen = defaultdict(int)
        for i, row in enumerate(matrix):
            if tuple(row) in seen or tuple(self.flip_row(row)) in seen:
                seen[tuple(row)] += 1
            else:
                seen[tuple(row)] += 1
    
        result = 0
        for val in seen.values():
            result = max(result, val)
        
        return result
