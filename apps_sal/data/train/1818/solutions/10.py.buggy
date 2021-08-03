# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def helper(root: TreeNode) -> str:
    if root is None:
        return [\"\"]
    
    s = chr(ord('a') + root.val)
    
    if root.left is None and root.right is None:
        return [s]
    elif root.left is None:
        return [_ + s for _ in helper(root.right)]
    elif root.right is None:
        return [_ + s for _ in helper(root.left)]
    else:
        left = [_ + s for _ in helper(root.left)]
        right = [_ + s for _ in helper(root.right)]

        return left + right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        return min(helper(root))
        
