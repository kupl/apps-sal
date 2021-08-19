class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        med = arr[int((len(arr) - 1) / 2)]
        print(med)
        f = []
        while len(f) < k:
            rv = abs(arr[-1] - med)
            lv = abs(arr[0] - med)

            # print(arr[-1],arr[0])
            # print(rv,lv)

            if rv >= lv:
                f.append(arr.pop(-1))
            else:
                f.append(arr.pop(0))

        return f
