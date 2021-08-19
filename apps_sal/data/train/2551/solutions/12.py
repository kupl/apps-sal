class Solution:

    def isValid(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')
        if s == '':
            return True
        else:
            return False
        '\n         :type s: str\n         :rtype: bool\n         '
