class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= k:
            return arr
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        i = 0
        j = len(arr) - 1
        result = []
        while k > 0:
            if self.isStronger(arr[i], arr[j], median):
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j -= 1
            k -= 1
        return result

    def isStronger(self, a, b, median):
        return abs(a - median) > abs(b - median) or (abs(a - median) == abs(b - median) and a > b)
