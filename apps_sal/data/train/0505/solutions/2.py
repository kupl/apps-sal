class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        total = 0
        new_s = ''
        recent_opens = []
        for char in s:
            if char == '(':
                total += 1
                new_s = ''.join((new_s, char))
                recent_opens.append(len(new_s) - 1)
            elif char == ')':
                total -= 1
                if total >= 0:
                    new_s = ''.join((new_s, char))
                    recent_opens.pop()
                else:
                    total = 0
            else:
                new_s = ''.join((new_s, char))
        if total > 0:
            for (count, index) in enumerate(recent_opens):
                total -= 1
                new_s = ''.join((new_s[:index - count], new_s[index - count + 1:]))
                if total <= 0:
                    break
        return new_s
