class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        new_str = ''
        left = 0
        right = 0
        for i in s:
            if i != '(' and i != ')':
                new_str += i
                continue
            if i == '(':
                left += 1
                new_str += i
                continue
            if i == ')':
                if left > 0:
                    left -= 1
                    new_str += i
        final_str = ''
        for i in range(len(new_str) - 1, -1, -1):
            if new_str[i] != '(' and new_str[i] != ')':
                final_str += new_str[i]
                continue
            if new_str[i] == ')':
                right += 1
                final_str += new_str[i]
                continue
            if new_str[i] == '(':
                if right > 0:
                    right -= 1
                    final_str += new_str[i]
        return final_str[::-1]
