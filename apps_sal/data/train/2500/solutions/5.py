class Solution:
    def maxPower(self, s: str) -> int:
        '''
            does: given a string s, the power of the string is the maximum length of 
                  a non-empty substring that contains only one unique character.
            parameters: s
            returns: the power of the string.
        '''
        letter = None
        length = 0
        max_length = 0

        for i in s:

            if i == letter:
                length += 1
                max_length = max(max_length, length)

            else:
                max_length = max(max_length, length, 1)
                length = 1
                letter = i
            print(i, max_length)

        return max_length
