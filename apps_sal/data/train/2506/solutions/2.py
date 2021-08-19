class Solution:

    def isIsomorphic(self, s1, s2):
        """ Optimized version.
        Time complexity: O(n). Space complexity: O(1), n is len(s1) == len(s2).
        """
        (count1, count2) = (0, 0)
        (dict1, dict2) = (dict(), dict())
        for i in range(len(s1)):
            if s1[i] in dict1:
                curr1 = dict1[s1[i]]
            else:
                count1 += 1
                dict1[s1[i]] = count1
                curr1 = dict1[s1[i]]
            if s2[i] in dict2:
                curr2 = dict2[s2[i]]
            else:
                count2 += 1
                dict2[s2[i]] = count2
                curr2 = dict2[s2[i]]
            if curr1 != curr2:
                return False
        return True
