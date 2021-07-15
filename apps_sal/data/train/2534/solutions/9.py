class Solution:
    def maxScore(self, s: str) -> int:
        lis = []
        for i in range(1, len(s)):
            num1 = 0
            num2 = 0
            s1 = s[:i]
            s2 = s[i:]
            for i in s1:
                if i == '0':
                    num1 += 1
            for i in s2:
                if i == '1':
                    num2 += 1
            lis.append(num1 + num2)
        lis.sort(reverse = True)
        return lis[0]

