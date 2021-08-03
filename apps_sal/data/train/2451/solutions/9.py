class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        return all(mag[letter] >= ransom[letter] for letter in ransom)
