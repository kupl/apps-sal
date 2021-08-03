class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        q = []
        ans = []

        for i in range(len(s)):
            if (s[i] == '('):
                q.append(i)
            elif (s[i] == ')'):

                if (len(q) == 0):
                    ans.append(i)
                else:
                    q = q[:-1]

        if (len(q) != 0):
            ans = ans + q

        new_s = ''
        for i in range(len(s)):
            if (not (i in ans)):
                new_s = new_s + s[i]

        return new_s
