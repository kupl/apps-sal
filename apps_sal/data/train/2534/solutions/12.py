class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        result = 0
        if n <= 1:
            return n
        for i in range(1, n):
            left = s[:i]
            right = s[i:n]
            leftZeroCount = 0
            rightOneCount = 0

            for j in range(len(left)):
                if left[j] == '0':
                    leftZeroCount += 1
            for k in range(len(right)):
                if right[k] == '1':
                    rightOneCount += 1
            if (leftZeroCount + rightOneCount) > result:
                result = leftZeroCount + rightOneCount
        return result
