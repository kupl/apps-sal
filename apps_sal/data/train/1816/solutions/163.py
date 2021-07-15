class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def getMins(t):
            h, m = list(map(int, t.split(\":\")))
            return (h*60) + m
        
        ans = set()
        inp = collections.defaultdict(list)
        
        for name, time in zip(keyName, keyTime):
            inp[name].append(getMins(time))
            
        for name, mList in inp.items():
            mList.sort()
            N = len(mList)
            
            for left in range(N-2):
                if mList[left+2]-mList[left] <= 60:
                    ans.add(name)
                    break
                
        return sorted(ans)
