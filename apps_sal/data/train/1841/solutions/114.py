class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        # print(arr)
        temp, res = [], []
        for i in range(len(arr)):
            temp.append(abs(arr[i] - m))
        # print(temp)
        zipped_pairs = zip(temp, arr)
        z = [x for _, x in sorted(zipped_pairs)]
        # print(z)
        return z[len(z) - k:]
