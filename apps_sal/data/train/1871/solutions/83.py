# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.mx = 0

        def dfs(node, visited):
            if node is None:
                return
            else:
                for v in visited:
                    if abs(v - node.val) > self.mx:
                        self.mx = abs(v - node.val)
            dfs(node.left, visited + [node.val])
            dfs(node.right, visited + [node.val])
            return
        dfs(root, [])
        return self.mx
