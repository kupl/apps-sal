class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        final = []
        D = {}
        for i in B :
            b_counter = collections.Counter(i)
            for j in b_counter:
                D[j] = max(b_counter[j], D.get(j,0))
        for i in A:
            flag = True
            w = collections.Counter(i)
            for d in D:
                if w.get(d) and w[d]>=D[d]:
                    pass
                else:
                    flag = False
                    break
            if flag : final.append(i)
        return final
