class Solution:

    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        d = {i: set(v) for (i, v) in enumerate(A)}
        res = []
        for i in range(len(A)):
            isSubset = False
            for j in range(len(A)):
                if i == j:
                    continue
                if not d[i] - d[j]:
                    isSubset = True
                    break
            if not isSubset:
                res.append(i)
        return res
