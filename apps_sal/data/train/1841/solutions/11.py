class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        mid = (len(arr) - 1) // 2
        m = arr[mid]
        temp = sorted(arr, key=lambda x: abs(x - m))
        return temp[-1 * k:]
