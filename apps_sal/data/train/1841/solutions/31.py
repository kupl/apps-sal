import heapq


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        for i in range(len(arr)):
            arr[i] = (abs(m - arr[i]), arr[i])
        arr.sort(reverse=True)
        return [arr[i][1] for i in range(k)]
