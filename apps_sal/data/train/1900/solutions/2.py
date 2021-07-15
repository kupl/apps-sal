class Wrapper:
     def __init__(self, node, val=None):
         self.node = node
         self.val = val
     
     def isInt(self):
         return self.val is not None
     
     def getValue(self):
         if self.node:
             return self.node
         
         return self.val
     
     def addValue(self, val):
         self.val += val
 
 class Solution:
     def testNode(self, node, newStack):
         acc = 0
         
         if node:
             newStack.append(Wrapper(node))
             acc += 1
         elif len(newStack):
             acc += 1
             if newStack[-1].isInt():
                 newStack[-1].addValue(1)
             else:
                 newStack.append(Wrapper(None, 1))
                 
         return acc
     
     def widthOfBinaryTree(self, root):
         """
         :type root: TreeNode
         :rtype: int
         """
         if not root:
             return 0
         
         stack = [Wrapper(root)] 
         res = 1
         
         while len(stack):
             newStack = []
             acc = 0
             
             for node in stack:
                 if node.isInt():
                     if len(newStack):
                         if newStack[-1].isInt():
                             newStack[-1].addValue(2 * node.getValue())
                         else:
                             newStack.append(Wrapper(None, 2 * node.getValue()))
 
                         acc += 2 * node.getValue()
                 else:
                     acc += self.testNode(node.getValue().left, newStack)
                     acc += self.testNode(node.getValue().right, newStack)
                 
             stack = newStack
             if len(newStack) and newStack[-1].isInt():
                 acc -= stack.pop().getValue()
             res = max(res, acc)
                     
         return res
