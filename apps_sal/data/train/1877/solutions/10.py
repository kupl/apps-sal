# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def helper(root, currsum, limit):
            if not root:
                return True
            currsum += root.val
            if root.left is None and root.right is None:
                return currsum < limit
            
            deleteme = [True, True]
            
            if root.left:
                should_del = helper(root.left, currsum, limit)
                if should_del:
                    del root.left
                    root.left = None
                deleteme[0] = should_del
            
            if root.right:
                should_del = helper(root.right, currsum, limit)
                if should_del:
                    del root.right
                    root.right = None
                deleteme[1] = should_del
            
            return all(deleteme)
        
        deleteroot = helper(root, 0, limit)
        if deleteroot:
            del root
            return None
        return root
