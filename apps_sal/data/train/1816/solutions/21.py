from collections import deque

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        usermap = {}
        ansmap = {}
        
        def strtomin(foo):
            return int(foo[0:2]) * 60 + int(foo[3:])
        
        def analyze(foo):
            d = deque()
            for i in foo:
                d.append(i)
                while d[0] < i - 60:
                    d.popleft()
                if len(d) >= 3:
                    return True
            return False
                
        
        for i in range(len(keyName)):
            name = keyName[i]
            time = strtomin(keyTime[i])
            
            if name not in usermap:
                usermap[name] = []
            usermap[name].append(time)

        for i in usermap:
            usermap[i].sort()
            if analyze(usermap[i]):
                ansmap[i] = True

        return sorted(ansmap.keys())
