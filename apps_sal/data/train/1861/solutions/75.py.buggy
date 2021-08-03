class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        import math
        from collections import defaultdict
        row_m = defaultdict(list)
        
        for x, y in points:
            row_m[x].append(y)
            
        sol = float(\"inf\")
        # print(rows)
        pairs = {}
        
        for x in sorted(row_m):
            row = row_m[x]
            for i in range(len(row)):                
                for j in range(i + 1, len(row)):
                    
                    candidate = tuple(sorted([row[i], row[j]]))
                    if candidate in pairs:
                        sol = min(
                            sol,
                            abs(pairs[candidate] - x) * abs(row[i] - row[j]),
                        )                        
                    
                    pairs[candidate] = x
        # print(pairs)
        if sol == float('inf'):
            return 0
        return sol
                
            
            
