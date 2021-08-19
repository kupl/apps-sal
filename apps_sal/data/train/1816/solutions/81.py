class Solution:
    def less(self, start, end):
        t1 = int(start[:2]) * 60 + int(start[3:])
        t2 = int(end[:2]) * 60 + int(end[3:])

        if int(end[:2]) < int(start[:2]):
            return True

        return (t2 - t1) > 60

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        for i in range(len(keyName)):
            d[keyName[i]].append(keyTime[i])

        w = []
        res = []
        # print(d)
        for p in list(d.keys()):
            times = d[p]
            w = []
            for t in sorted(times):
                w.append(t)
                while w and self.less(w[0], t):
                    w.pop(0)

                if len(w) >= 3:
                    res.append(p)
                    break

        res.sort()
        return res
