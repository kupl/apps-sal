class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        l = [0] * (len(nums) + 1)
        nums.sort(reverse=True)
        for i in req:
            l[i[0]] += 1
            l[i[1] + 1] -= 1
        for i in range(1, len(l)):
            l[i] += l[i - 1]
        l = l[:-1]
        d = collections.defaultdict(list)
        for i in range(len(l)):
            d[l[i]].append(i)
        di = collections.OrderedDict(sorted(d.items()))
        k = 0
        ans = [0] * len(nums)
        for i in di:
            for j in di[i]:
                ans[j] = nums[len(nums) - k - 1]
                k += 1
        c = 0
        print(ans)
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]

        ans.insert(0, 0)
        print(ans)
        for i in req:
            c += (ans[i[1] + 1] - ans[i[0]])
        return c % (10**9 + 7)
