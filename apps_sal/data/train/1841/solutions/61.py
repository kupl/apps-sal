class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        l = len(arr)
        if l % 2 == 0:
            median = arr[(l - 1) // 2]
        else:
            median = arr[l // 2]
        print(median)
        s = sorted(arr, key=lambda x: (-abs(x - median), -x))
        print(s)
        return s[:k]
