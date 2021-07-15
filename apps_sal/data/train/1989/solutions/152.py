class Solution:
    def longestAwesome(self, s: str) -> int:
        mask_dict = { 0: -1 } #mask -> lowest_id
        answer = 0
        nums = list(map(int, s))
        mask = 0
        print(nums)
        for i in range(len(nums)):
            mask = mask ^ (1 << nums[i])
            if mask in mask_dict:
                answer = max(answer, i - mask_dict[mask])
            #check for odd num
            for j in range(10):
                n_mask = mask ^ (1 << j)
                if n_mask in mask_dict:
                    answer = max(answer, i - mask_dict[n_mask])

            if mask not in mask_dict: mask_dict[mask] = i
                
        print(mask_dict)
        return answer

