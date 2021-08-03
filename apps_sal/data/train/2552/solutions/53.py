class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        minCount = len(arr) // 4
        temp = 0
        pp = 0
        for i in range(len(arr)):
            if pp == arr[i]:
                temp += 1
            else:
                temp = 0
            if temp >= minCount:
                return arr[i]
            pp = arr[i]

        # from collections import Counter
        # c = Counter(arr)
        # return list(c.most_common(1))[0][0]
