class Solution:
    def maxPower(self, s: str) -> int:
        # Assign variables
        ans = 0
        consec_count_per_letter = 1
        prev_letter = s[0]

        # Return 1 when the length of the input is 1
        if len(s) == 1:
            return 1

        # Loop from 1 to the length of the input
        for i in range(1, len(s)):
            # If the current letter is the same as the prev letter,
            # then add 1 to consec_count_per_letter
            if s[i] == prev_letter:
                consec_count_per_letter += 1
            else:
                consec_count_per_letter = 1

            # Update the prev letter
            prev_letter = s[i]
            # Update the answer with a maximum
            # between the answer and consec_count_per_letter
            ans = max(ans, consec_count_per_letter)

        return ans
