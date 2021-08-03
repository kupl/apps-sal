class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        perm = [i for i in range(1, m + 1)]
        for element in queries:
            ind = perm.index(element)
            result.append(ind)
            tmp = [element]
            tmp.extend(perm[:ind])
            tmp.extend(perm[ind + 1:])
            perm = tmp
            print(perm)

        return result
