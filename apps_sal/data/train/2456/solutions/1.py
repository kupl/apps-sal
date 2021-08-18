class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def test(s):
            stack = []
            for l in s:
                if l == '
                if len(stack) != 0:
                    stack.pop()
                else:
                    stack.append(l)
            return ''.join(stack)

        return test(S) == test(T)
