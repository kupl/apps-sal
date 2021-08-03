class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        res = set()
        d = collections.defaultdict(list)
        for key, time in zip(keyName, keyTime):
            hour = int(time[:2])
            minute = int(time[3:])
            d[key].append(60 * hour + minute)
        for key, times in d.items():
            if key not in res:
                times.sort()
                q = deque()
                for time in times:
                    q.append(time)
                    while q and (q[-1] - q[0]) % (24 * 60) > 60:
                        q.popleft()
                    if len(q) >= 3:
                        res.add(key)
                        break
        return sorted(res)
