class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        paren_arr = []
        paren_stack = []
        index = 0
        for c in s:
            if c != ')' and c != '(':
                continue
            elif c == '(':
                paren_arr.append(c)
                paren_stack.append((c, index))
                index += 1
            else:
                paren_arr.append(c)
                if len(paren_stack) > 0 and paren_stack[-1][0] == '(':
                    paren_stack.pop()
                else:
                    paren_stack.append((c, index))
                index += 1
        for e in paren_stack:
            paren_arr[e[1]] = '-'
        s_arr = []
        index = 0
        while index < len(paren_arr) and paren_arr[index] == '-':
            index += 1
        for c in s:
            if c != ')' and c != '(':
                s_arr.append(c)
            elif index < len(paren_arr) and c == paren_arr[index]:
                s_arr.append(c)
                index += 1
                while index < len(paren_arr) and paren_arr[index] == '-':
                    index += 1
        return ''.join(s_arr)
