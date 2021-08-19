class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = [i + 1 for i in range(m)]
        out = []
        for i in queries:
            idx = perm.index(i)
            out.append(idx)
            temp = perm[idx]
            while idx > 0:
                perm[idx] = perm[idx - 1]
                idx -= 1
            perm[idx] = temp
        return out
