class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        tm = list(map(lambda x: int(x.split(':')[0])*60 + int(x.split(':')[1]), keyTime))
        ans = set()
        tmp = []
        for name, tm in zip(keyName, tm):
            tmp.append((tm, name))
        
        tmp.sort()
        d = defaultdict(deque)
        for time, name in tmp:
            # print(name, time)
            while d[name] and abs(time - d[name][0]) > 60:
                d[name].popleft()
            d[name].append(time)
            
            if len(d[name]) >= 3:
                ans.add(name)
            
        return sorted(ans)
