class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n+1):
            s = sum([int(x) for x in str(i)])
            d[s] = d.get(s, []) + [i]
        nums = [len(d[x]) for x in d]
        d = collections.Counter(nums)
        return d[max(nums)]

