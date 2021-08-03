class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters is None or len(letters) == 0:
            return None
        start, end = 0, len(letters) - 1
        while(start + 1 < end):
            mid = start + (end - start) // 2
            if(letters[mid] <= target):
                start = mid
            else:
                end = mid
        if(letters[start] > target):
            return letters[start]
        elif(letters[end] > target):
            return letters[end]
        else:
            return letters[0]
