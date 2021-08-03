class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()
        if s == '':
            return True
        wordsR = []
        for item in s:
            if item.isalnum() == True:
                wordsR.append(item)
        if wordsR == []:
            return True
        words = wordsR[:]
        wordsR.reverse()
        if words == wordsR:
            return True
        else:
            return False
