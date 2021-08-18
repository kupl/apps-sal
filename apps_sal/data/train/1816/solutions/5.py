class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        records = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            minutes, seconds = int(time[:2]), int(time[-2:])
            records[name].append(60 * minutes + seconds)
        res = []
        for name in records:
            q = collections.deque()
            found = False
            for time in sorted(records[name]):
                while q and abs(time - q[0]) > 60:
                    q.popleft()
                q.append(time)
                if len(q) >= 3:
                    found = True
                    break
            if found:
                res.append(name)
        return sorted(res)
