class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]
        height = target[0]
        for val in target[1:]:
            if val > height:
                count += val - height
            height = val
        return count
