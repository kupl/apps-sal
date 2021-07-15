# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def construct(preorder):
            if len(preorder) == 0:
                return None
            root = TreeNode(preorder[0])
            #   开始分裂
            idx = 0
            while idx < len(preorder):
                if preorder[idx] > preorder[0]:
                    break
                idx += 1
            root.left  = construct(preorder[1:idx])
            root.right = construct(preorder[idx:])
            return root
        root = construct(preorder)
        return root

