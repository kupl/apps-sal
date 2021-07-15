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
 
 class Solution:
     def deserialize(self, s):
         """
         :type s: str
         :rtype: NestedInteger
         """
         
         root_ni = NestedInteger()
         
         ni_stack = collections.deque()
         current_ni = root_ni
         
         active_number = None
         is_positive = True
         
         for i, c in enumerate(s):
             if c == '-':
                 is_positive = False
                 active_number = 0
 
             elif c.isdigit():
                 # Check if the previous was a digit as well.
                 if active_number is None:
                     active_number = int(c)
                 else:
                     active_number = int(c) + active_number * 10
 
             else:
                 if active_number is not None:
                     if not is_positive:
                         active_number *= -1
 
                     current_ni.add(active_number)
                     active_number = None
                     is_positive = True
 
                 if c == '[' and i > 0:
                     ni_stack.append(current_ni)
                     current_ni = NestedInteger()
 
                 elif c == ']' and len(ni_stack) > 0:
                     ni_stack[-1].add(current_ni)
                     current_ni = ni_stack.pop()
 
         if active_number is not None:
             if not is_positive:
                 active_number *= -1
 
             if not current_ni.getList():
                 current_ni.setInteger(active_number)
             else:
                 current_ni.add(active_number)
             
         return root_ni
         
         
