class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        res = []
        valuearr = []
        arr.sort()
        m = arr[int((len(arr)-1)/2)]
        # if len(arr) % 2 == 0:
        #     m = (arr[int(len(arr) / 2)] + arr[int(len(arr) / 2 - 1)]) / 2
        # else:
        #     m = arr[int((len(arr) - 1) / 2)]

        for i in arr:
            value = []
            value.append(i)
            value.append(abs(i - m))
            valuearr.append(value)

        valuearr.sort(key=lambda x: (x[1], x[0]), reverse=True)

        for i in range(k):
            res.append(valuearr[i][0])

        # if valuearr[k-1][1] != valuearr[k][1]:
        #     res.append(valuearr[k-1][0])
        # else:
        #     if valuearr[k-1][0] > valuearr[k][0]:
        #         res.append(valuearr[k-1][0])
        #     else:
        #         res.append(valuearr[k][0])

        return res
