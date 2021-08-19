class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sum = 0
        i = 0
        ans = ''
        opens = []
        while(i < len(s)):
            if s[i] == '(':
                sum += 1
            elif s[i] == ')':
                sum -= 1
            if sum < 0:
                sum = 0
                i += 1
            else:
                ans += s[i]
                if ans[-1] == '(':
                    opens.append(len(ans) - 1)
                i += 1
        if sum == 0:
            return ans
        while(sum > 0):
            # find last index
            index = opens[-1]
            opens = opens[:-1]
            ans = ans[:index] + ans[index + 1:]
            sum -= 1
        return ans
