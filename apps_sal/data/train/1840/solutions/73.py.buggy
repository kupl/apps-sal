# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def zigzag(node, direction, mz):
            if not node:
                return -1
            if direction == \"l\":
                zigzag(node.left, \"l\", mz)
                c = zigzag(node.left, \"r\", mz)+1
            else:
                zigzag(node.right, \"r\", mz)
                c = zigzag(node.right, \"l\", mz)+1
            mz[0] = max(mz[0], c)
            return c

        maxzigzag = [0]
        zigzag(root, \"l\", maxzigzag)
        zigzag(root, \"r\", maxzigzag)

        return maxzigzag[0]

