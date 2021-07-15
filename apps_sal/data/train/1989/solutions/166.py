class Solution:
    def longestAwesome(self, s: str) -> int:
        mask_dict = {0: -1}
        mask = 0
        max_length = 0
        for i, ch in enumerate(s):
            # even
            mask ^= (1 << (ord(ch) - ord('0')))
            if mask in mask_dict:
                max_length = max(max_length, i - mask_dict[mask])
            # odd
            for j in range(10):
                mask_odd = mask ^ (1 << j)
                if mask_odd in mask_dict:
                    max_length = max(max_length, i - mask_dict[mask_odd])
                    
            if not mask in mask_dict:
                mask_dict[mask] = i
        return max_length
            

