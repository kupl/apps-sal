# """
 # This is the interface that allows for creating nested lists.
 # You should not implement it, or speculate about its implementation
 # """
 #class NestedInteger:
 #    def __init__(self, value=None):
 #        """
 #        If value is not specified, initializes an empty list.
 #        Otherwise initializes a single integer equal to value.
 #        """
 #
 #    def isInteger(self):
 #        """
 #        @return True if this NestedInteger holds a single integer, rather than a nested list.
 #        :rtype bool
 #        """
 #
 #    def add(self, elem):
 #        """
 #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 #        :rtype void
 #        """
 #
 #    def setInteger(self, value):
 #        """
 #        Set this NestedInteger to hold a single integer equal to value.
 #        :rtype void
 #        """
 #
 #    def getInteger(self):
 #        """
 #        @return the single integer that this NestedInteger holds, if it holds a single integer
 #        Return None if this NestedInteger holds a nested list
 #        :rtype int
 #        """
 #
 #    def getList(self):
 #        """
 #        @return the nested list that this NestedInteger holds, if it holds a nested list
 #        Return None if this NestedInteger holds a single integer
 #        :rtype List[NestedInteger]
 #        """
 
 import re
 
 class Solution:
     def deserialize(self, s):
         """
         :type s: str
         :rtype: NestedInteger
         """
         s = re.sub("\[","[,", s)
         s = re.sub("\]",",]", s)
         s = s.split(",")
 
         if not s[0] == "[":
             return NestedInteger(int(s[0]))
         
         obj = NestedInteger()
         self.parse_recursive_list(s, 1, obj)
         return obj
         
     def parse_recursive_list(self, s, i, obj):
         while i<len(s):
             if s[i] == '':
                 i += 1
                 continue
             if s[i] == "[":
                 new_obj = NestedInteger()
                 i = self.parse_recursive_list(s, i+1, new_obj)
                 obj.add(new_obj)
             elif s[i] == ']':
                 return i+1
             else:
                 integer = int(s[i])
                 obj.add(NestedInteger(integer))
                 i += 1
         return i
             
                 
                 
