class Solution:

    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            sum = 0
            s = str(i)
            for c in s:
                sum += int(c)
            if sum in d:
                d[sum].append(i)
            else:
                d[sum] = [i]
        values = list(d.values())
        values.sort(key=len, reverse=True)
        count = 0
        length = len(values[0])
        for v in values:
            if length == len(v):
                count += 1
        return count
