class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        l = []
        i = 0
        j = len(arr) - 1
        while i <= j:
            if abs(arr[i] - m) > abs(arr[j] - m):
                l.append(arr[i])
                i = i + 1
            elif abs(arr[i] - m) <= abs(arr[j] - m):
                l.append(arr[j])
                j = j - 1
            if len(l) == k:
                return l
