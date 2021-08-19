class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        sl = list(s)

        def sweep(begin, end, step, open_symbol, close_symbol):
            level = 0
            k = begin
            for i in range(begin, end, step):
                if sl[i] == open_symbol:
                    level = max(level, 0) + 1
                elif sl[i] == close_symbol:
                    level -= 1
                if not (level < 0 and sl[i] == close_symbol):
                    sl[k] = sl[i]
                    k += step
            return k - step
        level = 0
        r = sweep(0, len(s), 1, '(', ')')
        l = sweep(r, -1, -1, ')', '(')
        return ''.join(sl[l:r + 1])
