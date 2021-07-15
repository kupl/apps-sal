# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 10:35
    def helper(self, root, path):
        if root == None:
            return path
        else:
            my_path = chr(ord('a') + root.val) + path
            left = self.helper(root.left, my_path)
            right = self.helper(root.right, my_path) 
            if root.left == None:
                ans = right
            elif root.right == None:
                ans = left
            else:
                ans = min(left, right)
            return ans
        
    def smallestFromLeaf(self, root: TreeNode) -> str:
        path = \"\"
        return self.helper(root, path)
