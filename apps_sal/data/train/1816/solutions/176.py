class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        M = defaultdict(list)
        
        for i,j in zip(keyName, keyTime):
            bisect.insort(M[i], j)
        
        keys = sorted(M.keys())
        
        res = []
        
        def getMins(time):
            return int(time[:2])*60 + int(time[3:])
        
        # print(M)
        
        for key in keys:
            for i in range(2, len(M[key])):
                curr = M[key][i]
                prev1 = M[key][i-2]
                if getMins(curr) - getMins(prev1) <= 60:
                    res.append(key)
                    break
        
        return res
