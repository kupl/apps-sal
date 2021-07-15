class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count_lst = [0]*(len(nums) + 1)
        for start, end in requests:
            count_lst[start] += 1
            count_lst[end + 1] -= 1
        # print(count_lst)    
        ret_lst = [0]*(len(nums) + 1)
        for i in range(len(ret_lst)):
            if i == 0 and count_lst[i] != 0:
                ret_lst[i] = count_lst[i]
                continue
            
            ret_lst[i] = ret_lst[i - 1] + count_lst[i]
        # print(ret_lst)
        ret_lst.sort(reverse = True)
        nums.sort(reverse = True)
        ret_num = 0
        
        for i in range(len(nums)):
            ret_num += ret_lst[i]*nums[i]
        return ret_num % (10**9 + 7)
