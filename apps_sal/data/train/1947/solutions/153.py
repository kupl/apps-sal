class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        s = set(A)
        d = {}
        for i in B:
            for j in i:
                count = i.count(j)
                if j not in d or count > d[j]:
                    d[j] = count

        for i in A:
            for j in d:
                if i.count(j) < d[j]:
                    s.remove(i)
                    break
        return list(s)
