# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        def rec(curr, deleted):
            nonlocal res
            if not curr:
                return None
            if curr.val in to_delete:
                curr.left = rec(curr.left, True)
                curr.right = rec(curr.right, True)
                
            else:
                curr.left = rec(curr.left, False)
                curr.right = rec(curr.right, False)
                if deleted:
                    res.append(curr)
            return None if curr.val in to_delete else curr
        rec(root, True)
        return res
