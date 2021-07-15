# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = node = TreeNode(preorder[0])
        stack = []
        
        for n in preorder[1:]:
            if n < node.val:
                node.left = TreeNode(n)
                stack.append(node)
                node = node.left
            else:
                while stack and stack[-1].val < n:
                    node = stack.pop()
                node.right = TreeNode(n)
                node = node.right
        return root
                    

