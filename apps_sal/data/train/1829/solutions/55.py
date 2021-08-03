# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        maximum = root.val
        self.count = 0

        def dfs(node, maximum):
            if not node:
                return
            if node.val >= maximum:
                self.count += 1
                maximum = max(maximum, node.val)
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, maximum)
        return self.count
