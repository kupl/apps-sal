class Solution:
    def longestAwesome(self, s: str) -> int:
        mask, res = 0, 1
        mask_pos = {0: -1}
        
        for i, c in enumerate(s):
            c = int(c)
            mask ^= (1 << c)
            for j in range(11):
                check_mask = 1023 & (mask ^ (1 << j))
                if check_mask in mask_pos:
                    res = max(res, i - mask_pos[check_mask])
            if mask in mask_pos:
                res = max(res, i - mask_pos[mask])
            else:
                mask_pos[mask] = i
        return res

