class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return s

        paranthesis_balance = 0
        ends = []

        for i, char in enumerate(s):
            if char == '(':
                paranthesis_balance += 1
            elif char == ')' and paranthesis_balance > 0:
                ends.append(i)
                paranthesis_balance -= 1
            else:
                continue

        starts = []
        paranthesis_balance = 0

        for i, char in enumerate(reversed(s)):
            if char == ')':
                paranthesis_balance += 1
            elif char == '(' and paranthesis_balance > 0:
                starts.append(len(s) - i - 1)
                paranthesis_balance -= 1
            else:
                continue

        balanced_str = []

        starts_i = len(starts) - 1
        ends_i = 0
        for i in range(len(s)):
            if starts_i >= 0 and i == starts[starts_i]:
                starts_i -= 1
                balanced_str.append('(')
            elif ends_i < len(ends) and i == ends[ends_i]:
                ends_i += 1
                balanced_str.append(')')
            elif s[i] not in {'(', ')'}:
                balanced_str.append(s[i])

        return ''.join(balanced_str)
