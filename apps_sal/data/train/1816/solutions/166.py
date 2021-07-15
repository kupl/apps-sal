class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = set()
        emp = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            h, m = list(map(int, time.split(':')))
            t = h*60 + m
            emp[name].append(t)
        for p, ts in list(emp.items()):
            ts.sort()
            tmp = deque(maxlen=3)
            for t in ts:
                tmp.append(t)
                if len(tmp) == 3 and tmp[0]+60>=tmp[-1]:
                    ans.add(p)
                    continue
        return sorted(ans)

