class Solution:
    def longestAwesome(self, s: str) -> int:
        left_most_masks = {0: -1}
        valid_masks = {1 << i for i in range(10)} | {0}
        ans = 0
        cur_mask = 0

        for idx, x in enumerate(list(s)):
            cur_mask = cur_mask ^ 1 << int(x)
            for valid_mask in valid_masks:
                left_mask = valid_mask ^ cur_mask
                if left_mask in left_most_masks:
                    ans = max(ans, idx - left_most_masks[left_mask])
            if cur_mask not in left_most_masks:
                left_most_masks[cur_mask] = idx
        return ans
