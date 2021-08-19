class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # time O(n); space O(1)
        return Counter(target) == Counter(arr)
