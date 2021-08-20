class Solution:

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        seen_character = False
        count = 0
        for char in s:
            if seen_character and char == ' ':
                count += 1
                seen_character = False
            elif seen_character == False and char != ' ':
                seen_character = True
        if seen_character:
            count += 1
        return count
