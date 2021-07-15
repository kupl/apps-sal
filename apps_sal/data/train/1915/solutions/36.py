class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        def helper(idx):
            num = len(stamp)
            for i in range(len(stamp)):
                if target[i+idx] == '*':
                    num -= 1
                elif target[i+idx] != stamp[i]:
                    return 0
            target[idx:idx+len(stamp)] = ['*']*len(stamp)
            return num
        
        seen = [0]*len(target)
        total = 0
        res = []
        target = list(target)
        while total < len(target):
            found = False
            for i in range(len(target)-len(stamp)+1):
                if seen[i] == 1: continue
                num = helper(i)
                if num == 0: continue
                seen[i] = 1
                total += num
                found = True
                res.append(i)
            if not found: return []
        return res[::-1]

