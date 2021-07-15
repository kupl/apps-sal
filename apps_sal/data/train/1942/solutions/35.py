class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        c_id = 0
        h = {}
        for fc in favoriteCompanies:
            for c in fc:
                if c in h:
                    continue
                h[c] = c_id
                c_id += 1
        for idx, fc in enumerate(favoriteCompanies):
            fc.sort(key=lambda x: h[x])
            
        N = len(favoriteCompanies)
        ret = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                ci, cj = favoriteCompanies[i], favoriteCompanies[j]
                iidx, jidx = 0, 0
                while iidx < len(ci) and jidx < len(cj):
                    iidx += ci[iidx] == cj[jidx]
                    jidx += 1
                if iidx == len(ci):
                    break
            else:
                ret.append(i)
        return ret 

