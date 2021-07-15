class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        idx = sorted(range(len(keyTime)), key=lambda i:keyTime[i])
        keyName = [keyName[i] for i in idx]
        keyTime.sort()
        self.D = collections.defaultdict(collections.deque)
        res =set()
        for n, t in zip(keyName, keyTime):
            self.D[n].append(t)
            #print(self.D[n][0], t)
            while self.expire(self.D[n][0], t):
                self.D[n].popleft()
            if len(self.D[n]) >= 3:
                res.add(n)
        return sorted(res)
    
    def expire(self, t1, t2):
        if t2[:2] == '00':
            if t1[:2] != '00':
                return True
            return t1 > t2
        if t1 > t2:
            return True
        tt = (int(t2[:2]) + 23) % 24
        return t1 < \"{:02d}{}\".format(tt, t2[2:])
