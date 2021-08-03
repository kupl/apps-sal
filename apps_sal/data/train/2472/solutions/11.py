class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydir = {}
        for record in s:
            mydir[record] = mydir.get(record, 0) + 1
        return mydir.get('A', 0) <= 1 and s.count('LLL') == 0
