class Solution:
    # def modifyString(self, s: str) -> str:
    #     if s == \"?\":
    #         return \"a\"
    #     for i in range(len(s)):
    #         if s[i] == '?':
    #             if i == 0:
    #                 print(\"right\")
    #                 for j in range(97,123):
    #                     if chr(j) != s[1]:
    #                         print(\"right\")
    #                         s = s.replace('?', chr(j), 1)
    #                         print(s)
    #                         break
    #             elif i == len(s)-1:
    #                 for j in range(97,123):
    #                     if chr(j) != s[i-1]:
    #                         s = s.replace('?', chr(j), 1)
    #                         break
    #             else:
    #                 for j in range(97,123):
    #                     if chr(j) != s[i-1] and chr(j) != s[i+1]:
    #                         s = s.replace('?', chr(j), 1)
    #                         break
    #     return s
    def modifyString(self, s: str) -> str:
        letters = ['a', 'b', 'c']
        for i in range(len(s)):
            if s[i] == '?':
                for l in letters:
                    if (i == 0 or s[i - 1] != l) and (i == len(s) - 1 or s[i + 1] != l):
                        s = s.replace('?', l, 1)
                        break

        return s
