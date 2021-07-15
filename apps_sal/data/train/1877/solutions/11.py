# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        head=TreeNode()
        head.left=root
        
        def inner1(root, prev_sum):
            if root is None:
                return
            else:
                root.val=(root.val, prev_sum)
                inner1(root.left, root.val[0]+prev_sum)
                inner1(root.right, root.val[0]+prev_sum)
                return
        
        def inner2(root):
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [sum(root.val)]
            left=inner2(root.left)
            if not left or max(left)<limit:
                root.left=None
            right=inner2(root.right)
            if not right or max(right)<limit:
                root.right=None
            res=left+right
            return res
        
        def inner3(root):
            if root is None:
                return
            else: 
                root.val=root.val[0]
                inner3(root.left)
                inner3(root.right)
                return
        
        inner1(head,0)
        _=inner2(head)
        inner3(head)
        return head.left
