class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        median = arr[int((len(arr) - 1) / 2)]
        strong = {}

        for x in arr:
            val = abs(x - median)
            if val not in list(strong.keys()):
                strong[abs(x - median)] = [x]
            else:
                strong[abs(x - median)].append(x)

        strong = sorted(list(strong.items()), reverse=True)
        strongest = []
        for x in strong:
            for val in sorted(x[1], reverse=True):
                if len(strongest) == k:
                    break
                strongest.append(val)

        return strongest
