class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        cands = [(n, int(t[:2]) * 60 + int(t[-2:])) for (n, t) in zip(keyName, keyTime)]
        cands.sort()
        rec = defaultdict(list)
        out = []
        for (n, t) in cands:
            if n in out:
                continue
            if n not in rec:
                rec[n].append(t)
            elif 0 <= abs(t - rec[n][0]) <= 60:
                rec[n].append(t)
            else:
                while rec[n] and abs(t - rec[n][0]) > 60:
                    rec[n].pop(0)
                rec[n].append(t)
                rec[n].sort()
            if len(rec[n]) == 3:
                out.append(n)
        return sorted(out)
