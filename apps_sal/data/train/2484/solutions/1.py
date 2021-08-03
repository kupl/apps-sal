class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        candidate, curr = '', ''

        for i in range(min(m, n)):
            if str1[i] != str2[i]:
                break
            else:
                curr += str1[i]
                if m % len(curr) == 0 and n % len(curr) == 0:
                    if str1 == curr * (m // len(curr)) and str2 == curr * (n // len(curr)):
                        candidate = curr

        return candidate
