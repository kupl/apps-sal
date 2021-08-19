# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lmemo = {}
        self.rmemo = {}

    def longestZigZag(self, root: TreeNode) -> int:
        def lzz(root, mx):
            if root is not None:
                lzz(root.left, mx)
                lzz(root.right, mx)
                mx[0] = max(mx[0], llzz(root), rlzz(root))
            return mx

        def llzz(root):
            if root not in self.lmemo:
                self.lmemo[root] = 1 + rlzz(root.left)
            return self.lmemo[root]

        def rlzz(root):
            if root not in self.rmemo:
                self.rmemo[root] = 1 + llzz(root.right)
            return self.rmemo[root]
        self.lmemo[None] = self.rmemo[None] = 0
        return lzz(root, [float('-inf')])[0] - 1
