class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open_chars = set(['(', '[', '{'])

        open_match = {')': '(', ']': '[', '}': '{'}

        open_stack = []

        for ch in s:

            if ch in open_chars:

                open_stack.append(ch)

            else:

                if not open_stack \
                        or open_stack[-1] != open_match[ch]:

                    return False

                open_stack.pop()

        return not open_stack
