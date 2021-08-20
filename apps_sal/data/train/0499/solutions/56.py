class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]
        avop = target[0]
        for i in range(1, len(target)):
            if avop < target[i]:
                count += target[i] - avop
            avop = target[i]
        return count
