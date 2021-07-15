class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        masks = {}
        
        for row, col in reservedSeats:
            masks[row] = masks.get(row, 0) + (1 << (10 - col))
        
        cnt = 2 * (n - len(masks))
        
        dbl_mask1, dbl_mask2 = 0b0111100000, 0b0000011110
        mdl_mask = 0b0001111000
        
        for row, mask in masks.items():
            cur = max(int((mask & dbl_mask1) == 0) + int((mask & dbl_mask2) == 0),
                      int((mask & mdl_mask) == 0))
            cnt += cur
        return cnt
