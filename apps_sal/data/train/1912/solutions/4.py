class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        res = ""
        if target == "z":
            target = "0"
        large = "z"

        found = False
        for i in range(len(letters)):
            if letters[i] > target and not found:
                found = True
                res = letters[i]
            elif found and not res < letters[i]:
                res = letters[i]
            elif letters[i] < large:
                large = letters[i]

        return large if len(res) == 0 else res
