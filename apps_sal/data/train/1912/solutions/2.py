class Solution:

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for idx in range(len(letters)):
            c = letters[idx]
            if c > target:
                return c
            if idx == len(letters) - 1:
                return letters[0]
