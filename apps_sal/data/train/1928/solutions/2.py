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
     def convertListToNestedInteger(self, nestList):
         if type(nestList) == type(0):
             return NestedInteger(nestList)
         rtype = NestedInteger()
         for item in nestList:
             if type(item) == type(0):
                 rtype.add(item)
             else:
                 nestedList = self.convertListToNestedInteger(item)
                 rtype.add(nestedList)
         return rtype
         
     def deserializeHelper(self, st):
         if len(st) > 0:
             if st[0] != '[':
                 return int(st)
         assert(len(st) > 1)
         assert(st[0] == '[')
         assert(st[-1] == ']')
         l = st[1:].find('[')
         r = st[:-1].rfind(']')
         assert(l*r >= 0)
         if l > 0:
             nums = [int(s) for s in st[1:l].split(',') if s.strip() != '']
             rest = self.deserializeHelper('[' + st[l+1:] )
             for item in rest:
                 nums.append(item)
             #nums.append(rest)
             return nums
         elif l < 0:
             nums = [int(s) for s in st[1:l].split(',') if s.strip() != '']
             return nums
         r = self.matchingBracket(st)
         ret = [self.deserializeHelper(st[l+1:r+1])]
         if st[r+1] != ']':
             rest = self.deserializeHelper('[' + st[r+2:])
             for item in rest:
                 ret.append(item)
         return ret
 
     def matchingBracket(self, st):
         sum = 1
         #print(st)
         for r in range(2,len(st)):
             #print(sum, st[r])
             if st[r] == '[':
                 sum += 1
             elif st[r] == ']':
                 sum -= 1
             if sum == 0:
                 return r
         raise Exception("Invalid String")
         return None
     
     def deserialize(self, s):
         """
         :type s: str
         :rtype: NestedInteger
         """
         nestList = self.deserializeHelper(s)
         return self.convertListToNestedInteger(nestList)
         
