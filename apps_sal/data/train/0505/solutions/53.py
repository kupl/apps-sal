class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:

        def validParentheses(s, left_closed=False):
            i = 0
            res = ''
            while i < len(s):
                _i = 1
                _s = s[i]
                if _s == '(':
                    (_res, __i, closed) = validParentheses(s[i + 1:], True)
                    _i += __i
                    if closed:
                        _s += _res
                    else:
                        _s = _res
                elif _s == ')':
                    if left_closed:
                        return (res + ')', i + 1, True)
                    else:
                        _s = ''
                else:
                    pass
                res += _s
                i += _i
            return (res, i, False)
        return validParentheses(s, False)[0]
