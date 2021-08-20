class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        strongs = []
        for num in arr:
            strongs.append((abs(num - m), num))
        strongs.sort(reverse=True)
        return [x[1] for x in strongs[:k]]
