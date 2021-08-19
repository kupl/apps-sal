class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # get 25% length of arr.
        div = len(arr) // 4
        # go through array and use div to check if an element spans to that length, if it does, special integer found.
        for i in range(len(arr) - div):
            if arr[i] == arr[i + div]:
                return arr[i]
