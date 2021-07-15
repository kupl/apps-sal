class Solution:
    # https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/383670/JavaC++Python-Why-not-O(N)
    def reverseParentheses(self, s: str) -> str:
        stack, pairs = [], {}
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pairs[i], pairs[j] = j, i
        i, d, res = 0, 1, []
        while i < len(s):
            if s[i] in '()':
                i = pairs[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)
    
    # O(n^2)
    def reverseParentheses1(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                chars = []
                while stack and stack[-1] != '(':
                    chars.append(stack.pop())
                stack.pop()
                for ch in chars:
                    stack.append(ch)
            else:
                stack.append(c)
        # e.g. \"a(bcdefghijkl(mno)p)q\"
        return ''.join(stack)

