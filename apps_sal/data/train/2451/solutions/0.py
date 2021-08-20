class Solution:

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransome = set(ransomNote)
        for i in ransome:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
