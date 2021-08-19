class Solution:

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        a = []
        s = 0
        for i in range(0, len(letters)):
            s = a.append(ord(letters[i]) - ord(target))
        min = 100
        for i in range(0, len(a) - 1):
            if ord(letters[i]) <= ord(target) and ord(letters[i + 1]) > ord(target):
                return letters[i + 1]
        if ord(letters[0]) - ord(target) == 0:
            return letters[1]
        else:
            return letters[0]
