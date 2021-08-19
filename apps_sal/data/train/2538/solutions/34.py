class Solution:

    def countLargestGroup(self, n: int) -> int:
        map = {}
        mx = 0
        for i in range(1, n + 1):
            tempSum = 0
            for j in str(i):
                tempSum += int(j)
            map[tempSum] = map.get(tempSum, []) + [i]
            mx = max(mx, len(map.get(tempSum)))
        res = 0
        for key in map.keys():
            if len(map.get(key)) == mx:
                res += 1
        return res
