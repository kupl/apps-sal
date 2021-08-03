# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        stack.append(cloned)

        while stack:
            v = stack.pop()
            if v.val == target.val:
                return v

            if v.left:
                stack.append(v.left)
            if v.right:
                stack.append(v.right)
