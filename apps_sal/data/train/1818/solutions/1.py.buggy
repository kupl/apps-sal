# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        \"\"\"
        8:00 AM
        
        \"\"\"
        if root == None:
            return \"\"
        result  = None
        
        charMappings = { i: chr(i+ord(\"a\")) for i in range(0, 26)}
        
        def helper(node, path):
            nonlocal result
            if node == None:
                return
            
            if node.left == None and node.right == None:
                char = charMappings.get(node.val)
                string = \"\".join(  ((path+[char])[::-1]) )
                if result == None or string < result:
                    result = string
                
                return
            char = charMappings.get(node.val)
            helper(node.left, path+[char])
            helper(node.right, path+[char])
            
        helper(root, [])
        return result
                
