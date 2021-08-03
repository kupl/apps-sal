class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = strs
        import os
        return os.path.commonprefix(strs)


#         for x in strs:
#            if prefix in x:
#                 print x
