class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        t = [int(s[:2]) * 60 + int(s[3:]) for s in keyTime]
        l = sorted(zip(keyName, t))
        d = collections.defaultdict(list)
        for (i, j) in l:
            d[i] += [j]
        out = []
        for (s, l) in list(d.items()):
            if len(l) < 3:
                continue
            for i in range(2, len(l)):
                if l[i] - l[i - 2] <= 60:
                    out.append(s)
                    break
        return out
