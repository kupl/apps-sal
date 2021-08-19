class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        open_bracket = set()
        redundant_indices = set()
        for i in range(len(s)):
            if s[i] == '(':
                open_bracket.add(i)
            elif s[i] == ')' and len(open_bracket) > 0:
                open_bracket.remove(max(open_bracket))
            elif s[i] == ')' and len(open_bracket) == 0:
                redundant_indices.add(i)
        if open_bracket:
            for bracket in open_bracket:
                redundant_indices.add(bracket)
        result = ''
        for i in range(len(s)):
            if i not in redundant_indices:
                result += s[i]
        return result
