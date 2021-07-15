class Solution:
    def flip_row(self, row):
        for i, val in enumerate(row):
            if val == 0:
                row[i] = 1
            else:
                row[i] = 0
        return row
       
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # each row: maintain list of indices to flip to 1 or 0 for equality
        # then need to find greatest intersection out of all those
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
