# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_small(self, arr: List[int], idx: int, min_val: float) -> int:
        for i in range(idx+1, len(arr)):
            if arr[i] < arr[idx] and arr[i] >= min_val:
                return i
            
        return -1
    
    def get_big(self, arr: List[int], idx: int, max_val: float) -> int:
        for i in range(idx+1, len(arr)):
            if arr[i] >= arr[idx] and arr[i] < max_val:
                return i
            
        return -1
        
    def helper(self, preorder: List[int], idx: int, min_val: float, max_val: float) -> TreeNode:
        if idx == -1:
            return None
        
        root = TreeNode(preorder[idx])
        left = self.get_small(preorder, idx, min_val)
        right = self.get_big(preorder, idx, max_val)
        
        root.left = self.helper(preorder, left, min_val, preorder[idx])
        root.right = self.helper(preorder, right, preorder[idx], max_val)
        
        return root
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.helper(preorder, 0, float(\"-inf\"), float(\"inf\"))
        
