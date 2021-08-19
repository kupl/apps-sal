class Solution:

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for note in ransomNote:
            if note not in magazine:
                return False
            else:
                INDEX = magazine.index(note)
                magazine = magazine[:INDEX] + magazine[INDEX + 1:]
        return True
