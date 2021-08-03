# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, path: List[int]) -> None:
            if root is None:
                return

            path = path + [root.val]

            if root.left is None and root.right is None:
                result.append(path)
            else:
                dfs(root.left, path)
                dfs(root.right, path)

        result = []
        dfs(root, path=[])
        return max([abs(max(arr) - min(arr)) for arr in result])
