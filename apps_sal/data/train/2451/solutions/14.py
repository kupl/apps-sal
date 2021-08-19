class Solution:

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_map = {}
        for char in ransomNote:
            if char in r_map:
                r_map[char] += 1
            else:
                r_map[char] = 1
        m_map = {}
        for char in magazine:
            if char in m_map:
                m_map[char] += 1
            else:
                m_map[char] = 1
        for (char, count) in r_map.items():
            if char not in m_map:
                return False
            if count > m_map[char]:
                return False
        return True
