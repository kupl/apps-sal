class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for log in logs:
            if log[:-1] == '..':
                result = max(0, result - 1)
            elif log[:-1] == '.':
                pass
            else:
                result += 1
        return result

