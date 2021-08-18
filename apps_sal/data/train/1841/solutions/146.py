class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        arr.sort()
        return sorted(arr, key=lambda num: (abs(num - arr[(len(arr) - 1) // 2]), num))[-k:]
