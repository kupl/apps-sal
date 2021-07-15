class Solution:
    # O(n^2) TLE
    def longestAwesome(self, s: str) -> int:
        count = 0
        digits = 0
        for c in s:
            c = int(c)
            digits ^= 1 << c
            if digits & (1 << c) != 0:
                count += 1
            else:
                count -= 1
        result = 0
        n = len(s)
        for i in range(n):
            digits2 = digits
            count2 = count
            for j in reversed(list(range(i, n))):
                if j-i+1 <= result or count2 <= 1:
                    result = max(result, j-i+1)
                    break
                c = int(s[j])
                digits2 ^= 1 << c
                if digits2 & (1 << c) != 0:
                    count2 += 1
                else:
                    count2 -= 1
            c = int(s[i])
            digits ^= 1 << c
            if digits & (1 << c) != 0:
                count += 1
            else:
                count -= 1
        return result
    
    # O(10n)
    def longestAwesome(self, s: str) -> int:
        digits = {}
        digits[0] = -1
        prefix = 0
        result = 0
        for i in range(len(s)):
            c = int(s[i])
            prefix ^= 1 << c
            if prefix in digits:
                result = max(result, i - digits[prefix])
            else:
                digits[prefix] = i
            for k in range(10):
                tmp = prefix ^ (1<<k)
                if tmp in digits:
                    result = max(result, i - digits[tmp])
        return result

