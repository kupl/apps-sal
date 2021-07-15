class Solution:
     def isIsomorphic(self, s1, s2):
         """ Optimized version.
         Time complexity: O(n). Space complexity: O(1), n is len(s1) == len(s2).
         """
         # encode strings
         count1, count2 = 0, 0
         dict1, dict2 = dict(), dict()
         for i in range(len(s1)):
             char1, char2 = s1[i], s2[i]  # current characters
             if char1 in dict1:
                 curr1 = dict1[char1]  # current index of character in s1
             else:
                 count1 += 1
                 dict1[char1] = count1
                 curr1 = dict1[char1]
             if char2 in dict2:
                 curr2 = dict2[char2]  # current index of character in s2
             else:
                 count2 += 1
                 dict2[char2] = count2
                 curr2 = dict2[char2]
             if curr1 != curr2:
                 return False
         return True

