class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        l = len(arr)
        s = sorted(arr)
        middle = (l - 1) // 2
        median = s[middle]
        distances = []
        for i in s:
            distances.append([abs(i - median), i])
        strong_sort = sorted(distances, key=lambda x: x[0])
        s = l - k
        res = [strong_sort[i][1] for i in range(s, l)]
        return res
