# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def helper(root,maxVal):
            if root is None:
                return 
            if root.val>=maxVal:
                maxVal=root.val
                self.count+=1
            helper(root.left,maxVal)
            helper(root.right,maxVal)
        helper(root,-11111)
        return self.count
#     def dfs(root, max_till_now):
#             if not root:
#                 return
            
#             if root.val >= max_till_now:
#                 max_till_now = root.val
#                 self.good_nodes += 1
                
#             dfs(root.left, max_till_now)
#             dfs(root.right, max_till_now)
        
#         dfs(root,-10001)
#         return self.good_nodes

