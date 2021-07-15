class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = {}
        for a in A:
            d[a] = Counter(a)
        cd = defaultdict(int)
        for b in B:
            for i in Counter(b):
                cd[i] = max(cd[i], Counter(b)[i])
        ret = []
        for k in d:
            t = True
            for c in cd:
                if c not in k or d[k][c] < cd[c]:
                    t = False
                    break
            if t:
                ret.append(k)
        return ret
