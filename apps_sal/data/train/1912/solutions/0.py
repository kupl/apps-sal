class Solution:

    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if ord(letters[-1]) <= ord(target):
            return letters[0]
        li = 0
        ri = len(letters) - 1
        while li <= ri:
            if li == ri:
                return letters[li]
            mi = li + (ri - li) // 2
            if ord(letters[mi]) > ord(target):
                ri = mi
            else:
                li = mi + 1
