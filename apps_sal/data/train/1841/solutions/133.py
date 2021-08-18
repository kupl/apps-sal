class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr = sorted(arr)
        mid = arr[(n - 1) // 2]

        def mykey(x):
            return (abs(x - mid), x)

        arr = sorted(arr, key=lambda x: (abs(x - mid), x))
        return arr[n - k:]
