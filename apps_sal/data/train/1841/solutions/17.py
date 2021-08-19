class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []
        valuearr = []
        arr.sort()
        m = arr[int((len(arr) - 1) / 2)]
        for i in arr:
            value = []
            value.append(i)
            value.append(abs(i - m))
            valuearr.append(value)
        valuearr.sort(key=lambda x: (x[1], x[0]), reverse=True)
        for i in range(k):
            res.append(valuearr[i][0])
        return res
