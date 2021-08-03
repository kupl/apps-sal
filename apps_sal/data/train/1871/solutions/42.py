# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDiff = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        currPath = []

        def dfs(currNode, currPath):
            if not currNode:
                if len(currPath) > 0:
                    self.maxDiff = max(self.maxDiff, max(currPath) - min(currPath))

                return

            currPath.append(currNode.val)

            dfs(currNode.left, currPath)
            dfs(currNode.right, currPath)

            currPath.pop()

        dfs(root, currPath)
        return self.maxDiff
