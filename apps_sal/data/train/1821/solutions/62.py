class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        mi = abs(min(nums))
        nums = [i + mi for i in nums]
        l = len(str(max(nums)))
        res = []
        for i in nums:
            if len(str(i)) == l:
                res.append(str(i))
                continue
            d = l - len(str(i))
            a = '0' * d + str(i)
            res.append(a)
        for i in range(l - 1, -1, -1):
            res = self.f(res, i)
        return [int(i) - mi for i in res]

    def f(self, res, i):
        count = {str(x): [] for x in range(10)}
        for j in res:
            count[j[i]].append(j)
        arr = []
        for j in '0123456789':
            if len(count[j]) == 0:
                continue
            for x in count[j]:
                arr.append(x)
        return arr
