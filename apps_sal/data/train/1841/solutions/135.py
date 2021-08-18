class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        m = arr[((n - 1) // 2)]

        arr.sort(key=lambda x: (abs(x - m), x), reverse=True)

        return arr[:k]
