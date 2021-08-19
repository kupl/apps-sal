def shiftRight(arr, i):
    ele = arr[i]
    for j in range(i, 0, -1):
        arr[j] = arr[j - 1]
    arr[0] = ele
    return arr


def findQ(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i


class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        arr = list(range(1, m + 1))
        for i in range(len(queries)):
            q = queries[i]
            j = findQ(arr, q)
            res.append(j)
            shiftRight(arr, j)
        return res
