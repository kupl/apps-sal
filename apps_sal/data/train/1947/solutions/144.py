class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def getFrequency(s):
            d = {}
            for l in s:
                d[l] = d.get(l, 0) + 1
            return d
        main = {}
        for b in B:
            f = getFrequency(b)
            for k in f.keys():
                main[k] = max(main.get(k, 0), f[k])
        out = []
        for a in A:
            leto = getFrequency(a)
            cont = False
            for k in main.keys():
                if leto.get(k, 0) < main[k]:
                    cont = True
                    break
            if not cont:
                out.append(a)
        return out
