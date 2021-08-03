# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import string
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:   
        def pathToLeaf(root, letters):
            nonlocal smallest
            if root:
                letters+=chr(root.val + ord('a'))
                if root.right == None and root.left == None:
                    reversed_letters = letters[::-1]
                    if smallest > reversed_letters:
                        smallest =  reversed_letters
                else:
                    pathToLeaf(root.left, letters)
                    pathToLeaf(root.right,  letters)
        
        smallest = \"~\"
        pathToLeaf(root, \"\")
        return smallest
            
