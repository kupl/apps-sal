class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return len(s) == 0
