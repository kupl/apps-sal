# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_length = float('-inf')
    
    def longestZigZag(self, root):
        return self.dfs(root)[2] - 1
    
    def dfs(self, root):
        if root is None: return [0, 0, 0]
        
        left_res = self.dfs(root.left)
        right_res = self.dfs(root.right)
        
        maxForSubtree = max(left_res[1], right_res[0]) + 1
        return [left_res[1] + 1, right_res[0] + 1, max(maxForSubtree, left_res[2], right_res[2])]    
    
#     def __init__(self):
#         self.max_length = float('-inf')
#         self.memo = {}

#     def longestZigZag(self, root: TreeNode) -> int:
#         self.dfs(root)
#         return self.max_length if self.max_length != float('-inf') else 0
# # O(n) time, O(n) space
    
#     def dfs(self, root):
#         if root is None: return

#         self.dfs(root.left)
#         self.dfs(root.right)
        
#         left_res = self.zigzag(root, True)
#         right_res = self.zigzag(root, False)
#         self.max_length = max(self.max_length, left_res - 1, right_res - 1)        
        
#     def zigzag(self, node, is_left):
#         if id(node) in self.memo: 
#             if is_left and self.memo[id(node)][0]:
#                 return self.memo[id(node)][0]                    
#             elif is_left is False and self.memo[id(node)][1]:
#                 return self.memo[id(node)][1]
#         if node is None:
#             return 0

#         res = 0
#         if is_left:
#             res += self.zigzag(node.left, False)
#         else:
#             res += self.zigzag(node.right, True)

#         length = res + 1            
#         memoized_res = self.memo.get(id(node), [None, None])
#         memoized_res[(0 if is_left else 1)] = length
#         self.memo[id(node)] = memoized_res
#         return res + 1        

