class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        a = len(arr) * 0.25
        value = 0
        a1 = int(a)

        print(a1)

        dict1 = {}

        for i in arr:
            dict1[i] = dict1.get(i, 0) + 1

        for i in arr:
            if dict1.get(i) > a1:
                value = i

        return value
