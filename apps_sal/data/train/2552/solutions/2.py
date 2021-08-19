class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        a = list(set(arr))
        print(a)
        per = 0
        i = 0
        while per <= 0.25:
            b = a[i]
            per = arr.count(a[i]) / len(arr)
            i += 1
        return b
