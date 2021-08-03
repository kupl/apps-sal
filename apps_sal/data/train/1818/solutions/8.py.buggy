# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import string
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:   
        def pathToLeaf(root, letters, alphabet):
            nonlocal smallest
            if root:
               # count_path+=root.val
                letters+=alphabet[root.val]
                if root.right == None and root.left == None:
                    reversed_letters = letters[::-1]
                    if smallest > reversed_letters:
                        smallest =  reversed_letters
                else:
                    pathToLeaf(root.left, letters, alphabet)
                    pathToLeaf(root.right,  letters, alphabet)
        
        alphabet = dict( (i, letter) for i, letter in enumerate(string.ascii_lowercase))
        smallest = \"~\"
        pathToLeaf(root, \"\", alphabet)
        return smallest
            
