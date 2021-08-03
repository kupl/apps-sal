class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        n = [0] * 128
        for c in magazine:
            n[ord(c)] += 1
        for c in ransomNote:
            v = n[ord(c)]
            if v == 0:
                return False
            n[ord(c)] = v - 1

        return True
