class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        correct = ['()', '[]', '{}']
        out = ''
        a = s
        while self.contains(a, correct):
            for sym in correct:
                a = a.replace(sym, '')
        if len(a) == 0:
            return True
        else:
            return False

    def contains(self, st, chars):
        for ch in chars:
            if ch in st:
                return True
        return False
