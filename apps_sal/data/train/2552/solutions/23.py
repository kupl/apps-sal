class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        k = list(set(arr))

        tmp = []

        size = len(arr)

        for i in k:
            tmp.append(arr.count(i))

        maximum = max(tmp)

        indexing = tmp.index(maximum)

        z = (maximum / size) * 100

        if(z >= 25):
            return (k[indexing])
        else:
            return 0
