# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def findNodes(root, path):
            nonlocal result
            if not root:
                return
            path = [*path, root.val]
            if max(path) <= root.val:
                result += 1
            findNodes(root.left, path)
            findNodes(root.right, path)
        findNodes(root, [])
        return result
