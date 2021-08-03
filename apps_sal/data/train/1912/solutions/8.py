class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for char in letters:
            if char > target:
                return char
        return letters[0]
