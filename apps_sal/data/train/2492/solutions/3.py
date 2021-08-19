class Solution:

    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in logs:
            if i == '../':
                depth = max(0, depth - 1)
            elif i != './':
                depth += 1
        return depth
