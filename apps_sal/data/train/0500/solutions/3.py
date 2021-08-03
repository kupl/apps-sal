class Solution:
    def calculate(self, s):
        if not s:
            return 0
        length = len(s)
        stack = []
        num = 0
        sign = '+'
        for idx, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            if c in ['+', '-', '*', '/'] or idx == length - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0

        return sum(stack)
        """
         :type s: str
         :rtype: int
         """
