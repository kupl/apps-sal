class Solution:
    def partition(self, arr, start, end):
        follower = leader = start
        while leader < end:
            if arr[leader] <= arr[end]:
                arr[leader], arr[follower] = arr[follower], arr[leader]
                follower += 1
            leader += 1
        arr[follower], arr[end] = arr[end], arr[follower]
        return follower
    
    def quicksort(self, arr, start, end):
        if start >= end:
            return
        else:
            p = self.partition(arr, start, end)
            self.quicksort(arr, p + 1, end)
            self.quicksort(arr, start, p - 1)
            
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        self.quicksort(arr, 0, len(arr) - 1)
        self.quicksort(target, 0, len(arr) - 1)
        return target == arr
    
    

