class Solution:

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1 = {i: [] for i in pattern}
        for (tag, i) in enumerate(pattern):
            dict1[i].append(tag)
        L1 = []
        for key in dict1:
            L1.append(dict1[key])
        dict2 = {i: [] for i in str.split()}
        for (tag, i) in enumerate(str.split()):
            dict2[i].append(tag)
        L2 = []
        for key in dict2:
            L2.append(dict2[key])
        if sorted(L1) == sorted(L2):
            return True
        else:
            return False
