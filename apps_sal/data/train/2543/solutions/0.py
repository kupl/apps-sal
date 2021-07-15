class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = [char for char in S if char.isalpha()]
        result = ''
        for char in S:
            if char.isalpha():
                temp = stack.pop()
                result += temp
            else:
                result += char
        return result
