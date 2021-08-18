class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        level = 0
        result = list(s)
        open_pos = []
        close_pos = []
        for i, c in enumerate(s):
            if c == '(':
                level += 1
                open_pos.append(i)
            elif c == ')':
                open_idx = None
                if open_pos:
                    open_idx = open_pos.pop()
                if level == 0:
                    if open_idx:
                        result[open_idx] = '_'
                    result[i] = '_'
                else:
                    level -= 1

        return ''.join([x for i, x in enumerate(result) if x != '_' and not i in open_pos])
