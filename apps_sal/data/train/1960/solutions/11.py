class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        A = list(range(1, m + 1))
        res = []
        for target in queries:
            for (i, num) in enumerate(A):
                if num == target:
                    res.append(i)
                    index = i
                    break
            element = A[index]
            A.pop(index)
            A.insert(0, element)
        return res
