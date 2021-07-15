class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        def flip(arr):
            for i in range(len(arr)):
                if arr[i] == 1:
                    arr[i] = \"#\"
                if arr[i] == 0:
                    arr[i] = 1
            for i in range(len(arr)):
                if arr[i] == \"#\":
                    arr[i] = 0
            return arr
        
        d = {}
        for i in matrix:
            if tuple(i) in d:
                d[(tuple(i))] += 1
            elif tuple(flip(i)) in d:
                d[(tuple(i))] += 1
            else:
                d[(tuple(i))] = 1
        
        return max(list(d.values()))
