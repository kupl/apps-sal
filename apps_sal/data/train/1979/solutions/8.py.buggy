class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        for hour in range(23, -1, -1):
            for minute in range(59, -1, -1):
                candidate = sorted([ hour // 10, hour % 10, minute // 10, minute % 10])
                if candidate == arr:
                    return \"%s%s:%s%s\" % (hour // 10, hour % 10, minute // 10, minute % 10)
        return \"\"

