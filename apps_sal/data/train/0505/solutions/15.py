class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        cleaned = {}
        stack = []
        for (i, ch) in enumerate(s):
            if ch == ')':
                if len(stack):
                    cleaned[i] = ')'
                    stack.pop()
                else:
                    cleaned[i] = ''
                continue
            if ch == '(':
                stack.append(i)
            cleaned[i] = ch
        output = []
        for item in cleaned.items():
            if item[0] not in stack:
                output.append(item[1])
        return ''.join(output)
