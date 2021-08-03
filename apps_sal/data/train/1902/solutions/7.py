class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for ndigit in range(1, 10):
            for i in range(1, 10 - ndigit + 1):
                x = i
                for j in range(ndigit - 1):
                    x = x * 10 + (i + j + 1)
                if x > high:
                    break
                if x >= low:
                    ans.append(x)
        return ans
