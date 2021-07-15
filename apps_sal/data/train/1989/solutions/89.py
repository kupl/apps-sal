class Solution:
    def longestAwesome(self, s: str) -> int:
        pattern = [False]*10
        # {pattern: end position}
        # d = collections.defaultdict(int)
        d = {tuple(pattern): -1} 
        res = 0
        for i,x in enumerate(s):
            num = int(x)
            pattern[num] = not pattern[num]
            # there are 2 cases can construct palidrome at positoin i
            # 1) current pattern == previous pattern
            # 2) current pattern has one bit diff for previous pattern
            # and length will be current position - previous position
        
            res = max(res, i - d.get(tuple(pattern),i))
                
            for k in range(10):
                new_pattern = pattern.copy()
                new_pattern[k] = not new_pattern[k] #one bit different
                res = max(res, i-d.get(tuple(new_pattern),i))
                    
            d.setdefault(tuple(pattern),i)
        return res
