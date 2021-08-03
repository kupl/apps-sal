class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        arr_len = len(arr)
        m = arr[(arr_len - 1) // 2]
        i, j = 0, arr_len - 1
        toret = []
        size = 0
        while i <= j and size < k:
            if abs(arr[i] - m) > abs(arr[j] - m):
                toret.append(arr[i])
                i += 1
            else:
                toret.append(arr[j])
                j -= 1
            size += 1
        return toret
