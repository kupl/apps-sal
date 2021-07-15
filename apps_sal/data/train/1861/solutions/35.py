class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        ret = float('inf')
        
        r_to_c = collections.defaultdict(list)
        
        for r, c in points:
            r_to_c[r].append(c)
            
        seen = {}
        
        for bottom in sorted(r_to_c.keys()):
            cols = r_to_c[bottom]
            cols.sort()
            
            for right_i in range(len(cols)):
                for left_i in range(right_i):
                    left = cols[left_i]
                    right = cols[right_i]
                    
                    if (left, right) in seen:
                        top = seen[(left, right)]
                        ret = min(ret, (bottom - top) * (right - left))
                    
                    seen[(left, right)] = bottom
                    
        
        
        
        if ret == float('inf'):
            return 0
        return ret
