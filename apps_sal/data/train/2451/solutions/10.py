class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        dic1 = collections.Counter(ransomNote)
        dic2 = collections.Counter(magazine)

        for key in dic1:
            if key not in dic2 or dic2[key] < dic1[key]:
                return False
        return True
