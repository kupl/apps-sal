class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sortedArr = sorted(arr)
        median = sortedArr[(len(sortedArr) - 1) // 2]
        strength = [[k, abs(k - median)] for k in sortedArr]
        strength = sorted(strength, key=lambda x: (x[1], x[0]), reverse=True)
        return [i[0] for i in strength[:k]]
