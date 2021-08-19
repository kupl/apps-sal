from string import ascii_lowercase as al


class Solution:

    def nextGreatestLetter(self, letters, target):
        """
            :type letters: List[str]
            :type target: str
            :rtype: str
            """
        index = ord(target) - 96
        s = set(letters)
        i = index
        for i in range(index + 1, index + 1 + 26 + 1):
            if chr((i - 1) % 26 + 96 + 1) in s:
                return chr((i - 1) % 26 + 96 + 1)
