class Solution:

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for letter in ransomNote:
            try:
                magazine.remove(letter)
            except ValueError:
                return False
        return True
