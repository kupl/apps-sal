class Solution:

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = collections.Counter(ransomNote)
        b = collections.Counter(magazine)
        for let in ransomNote:
            if a[let] > b[let]:
                return False
        return True
