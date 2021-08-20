class Solution:

    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        l = []
        counts = 0
        visited = True
        for i in range(len(arr) - 1):
            counts = arr.count(arr[i])
            if counts == arr[i] and visited:
                l.append(arr[i])
                counts = 0
            if arr[i] == arr[i + 1]:
                visited = False
            else:
                visited = True
        if len(l) != 0:
            return max(l)
        else:
            return -1
