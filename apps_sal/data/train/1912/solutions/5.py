class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        curr_small = None
        for letter in letters:
            if letter > target:
                if curr_small == None or curr_small > letter:
                    curr_small = letter
        if curr_small:
            return curr_small
        else:
            return letters[0]
