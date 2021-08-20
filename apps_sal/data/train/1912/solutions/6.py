class Solution:

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        tmp = list(map(ord, letters))
        d = [x - y for (x, y) in zip(tmp, [ord(target)] * len(letters))]
        for i in range(len(d)):
            if d[i] <= 0:
                d[i] = 26 + d[i]
        return letters[d.index(min(d))]
