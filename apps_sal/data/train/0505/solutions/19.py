class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        p_stack = []
        new_string = ''

        def add_char(s: str, new: str) -> str:
            added = s + new
            return added

        def tmp_change(s: str, chg: int) -> str:
            new = s[:chg] + '0' + s[chg + 1:]
            return new

        def end_change(s: str) -> str:
            new = ''
            for i in range(0, len(s)):
                if s[i] != '0':
                    new = add_char(new, s[i])
            return new
        for i in range(0, len(s)):
            if s[i] == '(':
                p_stack.append(i)
                new_string = add_char(new_string, s[i])
            elif s[i] == ')':
                if len(p_stack) > 0:
                    p_stack.pop()
                    new_string = add_char(new_string, s[i])
                else:
                    new_string = add_char(new_string, '0')
            else:
                new_string = add_char(new_string, s[i])
        if p_stack != []:
            for i in p_stack:
                new_string = tmp_change(new_string, i)
            print(new_string)
        no_zeroes = end_change(new_string)
        print(no_zeroes)
        return no_zeroes
