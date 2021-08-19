class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # sortedArr = sorted(arr)
        # arr.sort()
        # median = sortedArr[(len(sortedArr) - 1) // 2]
        # # strength = [[k, abs(k - median)] for k in sortedArr]
        # strength = sorted(sortedArr, key=lambda x: (abs(x - median), x), reverse=True)
        # # print(strength)
        # return [i for i in strength[:k]]
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        # strength = [[k, abs(k - median)] for k in sortedArr]
        strength = sorted(arr, key=lambda x: (abs(x - median), x), reverse=True)
        # print(strength)
        return [i for i in strength[:k]]
