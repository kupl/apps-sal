class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = {}
        for e in B:
            tmp = {}
            for c in e:
                if c not in tmp:
                    tmp.update({c: 1})
                else:
                    tmp[c] += 1
            if not d or not tmp:
                d.update(tmp)
            else:
                for (k, v) in list(tmp.items()):
                    if k in d:
                        if v > d[k]:
                            d[k] = v
                    else:
                        d.update({k: v})
        if not d:
            return A
        ans = []
        for a in A:
            tmp = {}
            f = True
            for e in a:
                if e not in tmp:
                    tmp.update({e: 1})
                else:
                    tmp[e] += 1
            for (k, v) in list(d.items()):
                if k in tmp:
                    if v <= tmp[k]:
                        pass
                    else:
                        f = False
                        break
                else:
                    f = False
                    break
            if f:
                ans.append(a)
        return ans
