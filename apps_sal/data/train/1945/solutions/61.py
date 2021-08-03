class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1
        return max(cache.values())

    '''
    
Counter({(0, 0, 0): 1})
===
Counter({(0, 0, 0): 1, (1, 1, 1): 1})
=========
Counter({(0, 0, 0): 1, (1, 1, 1): 1, (0, 0, 1): 1})
=========
Counter({(0, 0, 0): 1, (1, 1, 1): 1, (0, 0, 1): 1, (1, 1, 0): 1})
=========
Counter({(1, 1, 0): 2, (0, 0, 0): 1, (1, 1, 1): 1, (0, 0, 1): 1})
=========
Counter({(0, 0, 1): 2, (1, 1, 0): 2, (0, 0, 0): 1, (1, 1, 1): 1})
=========
    '''
