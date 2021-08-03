class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        a = []
        for i in arr:
            if i == arr.count(i):
                a.append(i)
        if a:
            return (max(a))
        else:
            return -1
