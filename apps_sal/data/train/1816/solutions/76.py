class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        names = defaultdict(set)
        for n, t in zip(keyName, keyTime):
            names[n].add(t)
        for name in names:
            names[name] = sorted(names[name])
        # print(names)
        
        def timediff(t1, t2):
            t1 = list(map(int, t1.split(':')))
            t2 = list(map(int, t2.split(':')))
            h = t2[0] - t1[0]
            m = (t2[1] - t1[1]) / 60
            return h + m
        
        ans = set()
        for name in names:
            start = 0
            count = 1
            cur = start + 1
            for i in range(cur, len(names[name])):
                diff = timediff(names[name][start], names[name][i])
                print(name, diff)
                if diff <= 1:
                    count += 1
                    if count == 3:
                        ans.add(name)
                        break
                else:
                    start += 1
        return sorted(ans)
