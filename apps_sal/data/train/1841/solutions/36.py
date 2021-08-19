class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        start, end = 0, len(arr) - 1
        res = []
        l = len(arr)
        med = arr[end // 2]
        def is_greater(x, y): return abs(x - med) > abs(y - med)
        while end >= start:
            # 3 cases - equality is a separate case
            if is_greater(arr[start], arr[end]):
                res.append(arr[start])
                start += 1
            else:
                res.append(arr[end])
                end -= 1
        return res[:k]
