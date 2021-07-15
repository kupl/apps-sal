class Solution:
    def longestAwesome(self, s: str) -> int:
        bit_mask_mapping = {
            tuple([0]*10): -1,
        }
        
        bit_mask = [0]*10
        max_len = 0
        for ch_i, ch in enumerate(s):
            cur_int = int(ch)
            bit_mask[cur_int] ^= 1
            bit_mask_str = tuple(bit_mask)
            if bit_mask_str in bit_mask_mapping:
                max_len = max(max_len, ch_i - bit_mask_mapping[bit_mask_str])
            for j in range(10):
                tmp_mask = tuple(bit_mask[:j] + [bit_mask[j]^1] + bit_mask[j+1:])
                if tmp_mask in bit_mask_mapping:
                    max_len = max(max_len, ch_i - bit_mask_mapping[tmp_mask])
            if bit_mask_str not in bit_mask_mapping:
                bit_mask_mapping[bit_mask_str] = ch_i
        return max_len

