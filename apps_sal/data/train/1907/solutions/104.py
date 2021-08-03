# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original, cloned, target):
            if original == target:
                return cloned
            if original.left:
                l = dfs(original.left, cloned.left, target)
                if l:
                    return l
            if original.right:
                r = dfs(original.right, cloned.right, target)
                if r:
                    return r

        return dfs(original, cloned, target)
