class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        threshold = len(arr) // 4
        numdic = {}
        for num in arr:

            if str(num) not in numdic:
                numdic[str(num)] = 1
            else:
                numdic[str(num)] += 1

            if numdic[str(num)] > threshold:
                return num
