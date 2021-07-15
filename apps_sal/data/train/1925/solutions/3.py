# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.inorder = sorted(preorder)
        self.preorder = preorder[::-1]
        n = len(preorder)
        self.m = { val:i for i, val in enumerate(self.inorder)}
        lo, hi = 0, n-1
        return self.dfs(lo, hi)
        
    def dfs(self, lo, hi):
        if lo > hi: return None
        
        val = self.preorder.pop()
        root = TreeNode(val)
        mid = self.m[val]
        root.left = self.dfs(lo, mid-1)
        root.right = self.dfs(mid+1, hi)
        
        return root
