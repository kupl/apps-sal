# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return None
        
        maxlength = 0
        stack = collections.deque()
        if root.left:
            stack.append((1, 1, root.left))
        if root.right:
            stack.append((1, 0, root.right))
        while stack:
            length, isleft, node = stack.pop()
            if isleft:
                if node.right:
                    stack.append((length + 1, 0, node.right))
                else:
                    maxlength = max(maxlength, length)
                if node.left:
                    stack.append((1, 1, node.left))
            else:
                if node.left:
                    stack.append((length + 1, 1, node.left))
                else:
                    maxlength = max(maxlength, length)
  
                if node.right:
                    stack.append((1, 0, node.right))
            
        return maxlength
            

