class Solution:

    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        """
        # 比赛用代码
        res = []
        A = [(v, i) for i, v in enumerate(A)]
        A.sort(key = lambda x: len(x[0]))
        A = A[::-1]
        visit = []
        for v, i in A:
            v = set(v)
            if visit:
                for t in visit:
                    if v.issubset(t):
                        break
                else:
                    res.append(i)
            else:
                res.append(i)
            visit.append(v)
        return sorted(res)
        """
        res = []
        fc = [set(f) for f in A]
        n = len(fc)
        for i in range(n):
            for j in range(n):
                if i != j and fc[i] & fc[j] == fc[i]:
                    break
            else:
                res.append(i)
        return res
