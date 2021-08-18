class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        if not keyName:
            return []
        n = len(keyName)
        for i in range(n):
            d[keyName[i]].append(keyTime[i])

        ans = []

        def delta(t1, t2):
            t1 = list(map(int, t1.split(':')))
            t2 = list(map(int, t2.split(':')))
            h1, m1 = t1
            h2, m2 = t2
            if h2 - h1 > 1 or (h2 - h1 == 1 and m2 > m1):
                return True
            return False
        for name in d:
            times = d[name]
            times.sort()
            cur = [times[0]]
            t = 1
            for i in range(1, len(times)):
                t = times[i]
                cur.append(t)
                while cur and delta(cur[0], t):
                    cur.pop(0)
                if len(cur) == 3:
                    ans.append(name)
                    break
        return sorted(ans)
