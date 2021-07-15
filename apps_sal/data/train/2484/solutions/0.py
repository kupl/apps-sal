class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        contender = ''
        for i in str1:
            contender += i
            if str1.count(contender) * len(contender) == len(str1) and str2.count(contender) * len(contender) == len(str2):
                break
        orig = contender
        ans = None
        while len(contender) <= len(str1) and len(contender) <= len(str2):
            t1 = str1.replace(contender, '')
            t2 = str2.replace(contender, '')
            if len(t1) == len(t2) == 0:
                ans = contender
            contender += orig
        return ans if ans else ''
