# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
    
    def h(self, node: TreeNode, left: bool) -> int:
        if not node:
            return 0
        if (node, left) not in self.memo:
            ret = 0
            if left and node.left is not None:
                ret = 1+self.h(node.left, False)
            elif not left and node.right is not None:
                ret = 1+self.h(node.right, True)
            self.memo[(node,left)] = ret
        return self.memo[(node,left)]
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        ret = [0]
        if root.left is not None:
            ret.extend([
                1+self.h(root.left, False),
                self.longestZigZag(root.left)
            ])
        if root.right is not None:
            ret.extend([
                1+self.h(root.right, True),
                self.longestZigZag(root.right)
            ])
        return max(ret)
                

