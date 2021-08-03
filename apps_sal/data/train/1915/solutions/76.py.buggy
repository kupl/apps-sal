class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if stamp not in target:
            return []

        m, n = len(stamp), len(target)
        cnt = 0
        res = []

        while cnt < 1000:

            for i in range(n-m+1):

                # check any partial overlap of a stamp with target
                if target[i:i+m] != \".\"*m and self.find(stamp, target[i:i+m]):
                    target = target[:i] + \".\"*m + target[i+m:]
                    res.append(i)
                    break
            else:
                return []
 
            if target == \".\" * n:
                return res[::-1]
            cnt += 1

        return []

    def find(self, stamp, target):
        for i in range(len(stamp)):
            if target[i] != \".\" and stamp[i] != target[i]:
                return False
        return True        
