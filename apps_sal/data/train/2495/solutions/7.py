from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr_counter = Counter(target)
        tgt_counter = Counter(arr)
        
        return arr_counter == tgt_counter
