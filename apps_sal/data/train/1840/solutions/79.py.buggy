#https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/discuss/534620/4-python-solutions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#        
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0  # nonlocal variable to store answer
\t\t
        def recurse(root):
\t\t\t# if null return -1 because length is defined 
\t\t\t# as the number of nodes visited - 1. 
            if not root: return (-1,-1) 
\t\t\t
\t\t\t# l1 is max path len if we go left from current node and r1 if we go right\t\t\t\t\t\t
            l1,r1 = recurse(root.left)
            l2,r2 = recurse(root.right)
\t\t\t# Notice that if we go left from current node then we have no other choice but
\t\t\t# to go right from node.left to make the path zigzag. 
            
\t\t\t# That is why  r1 + 1 is the max path len  if we go left from current node. 
\t\t\t# Same logic for l2 + 1
            print(root.val,r1,l2)
            self.ans = max(self.ans, max(r1 + 1, l2 + 1))#r1 + 1, l2 + 1
            print(self.ans)
            
            return (r1 + 1, l2 + 1)
\t\t\t
        recurse(root)
        return self.ans
