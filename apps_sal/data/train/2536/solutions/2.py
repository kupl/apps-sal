class Solution:

    def findLucky(self, arr: List[int]) -> int:
        largest = 0
        a = {}
        for i in arr:
            if i in a:
                a[i] = a[i] + 1
            else:
                a[i] = 1
        for k in a:
            if a[k] == k:
                if k > largest:
                    largest = k
        return largest if largest else -1
