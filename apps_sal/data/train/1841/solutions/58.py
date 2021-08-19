class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        out = []
        arr.sort()
        l = 0
        h = len(arr) - 1
        m = arr[int(h / 2)]
        while l <= h:
            if abs(arr[l] - m) > abs(arr[h] - m):
                out.append(arr[l])
                l += 1
            else:
                out.append(arr[h])
                h -= 1
        return out[0:k]
