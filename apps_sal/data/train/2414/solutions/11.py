class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goodPairs = 0
        for (item, val) in enumerate(arr):
            restNums = arr[item + 1:]
            for (item2, val2) in enumerate(restNums):
                restNums2 = restNums[item2 + 1:]
                for (item3, val3) in enumerate(restNums2):
                    if abs(val - val2) <= a:
                        if abs(val2 - val3) <= b:
                            if abs(val - val3) <= c:
                                goodPairs += 1
        return goodPairs
