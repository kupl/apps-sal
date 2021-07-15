class Solution:
    def maxPower(self, s: str) -> int:
        '''
            does: given a string s, the power of the string is the maximum length of 
                  a non-empty substring that contains only one unique character.
            parameters: s
            returns: the power of the string.
        '''
        # initialize the letter to None
        letter = None
        # initialize the temporary length and maximum length to 0
        length = 0
        max_length = 0

        # loop through the string
        for i in s:

            # if encountered the same letter, length plus one
            if i == letter:
                length += 1
                # set maximum length to the max of (max_length, length, 1)
                max_length = max(max_length, length)

            # if encountered a different letter
            else:
                # set maximum length to the max of (max_length, length, 1)
                max_length = max(max_length, length, 1)
                # reset the length to 0
                length = 1
                # reset the target to current letter
                letter = i
            print(i, max_length)

        return max_length
