def median(arr: List[int]) -> int:
    arr.sort()
    m = int((len(arr) - 1) / 2)
    return arr[m]


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = median(arr)
        strength = [abs(x - m) for x in arr]
        zipped = list(zip(strength, arr))
        zipped.sort(key=lambda x: (x[0], x[1]))

        return [x[1] for x in zipped[(len(arr) - k):]]
