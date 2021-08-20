class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        (start_dic, end_dic) = ({}, {})
        modd = 10 ** 9 + 7
        for req in requests:
            (st, ed) = req
            start_dic[st] = start_dic.get(st, 0) + 1
            end_dic[ed] = end_dic.get(ed, 0) + 1
        idx_cnt = []
        cnt = 0
        for i in range(n):
            if i in start_dic:
                cnt += start_dic[i]
            if i - 1 in end_dic:
                cnt -= end_dic[i - 1]
            idx_cnt.append(cnt)
        idx_cnt.sort()
        nums.sort()
        res = [idx_cnt[i] * nums[i] for i in range(n)]
        ans = 0
        for x in res:
            ans = (ans + x) % modd
        return ans
