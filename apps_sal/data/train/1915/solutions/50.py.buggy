class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if stamp not in target:
            return []
        
        m, n = len(stamp), len(target)
        cnt = 0
        res = []
        
        while cnt < 10:
            flag = False
            for i in range(n-m+1):
                if target[i:i+m] != \".\"*m and self.helper(stamp, target[i:i+m]):
                    flag = True
                    target = target[:i] + \".\"*m + target[i+m:]
                    res.append(i)
                    
            if target == \".\"*n:
                return res[::-1]
            if not flag:
                return []
        cnt += 1
            
        return []
    
    def helper(self, stamp, target):
        for i in range(len(stamp)):
            if target[i] != \".\" and stamp[i] != target[i]:
                return False
        return True
