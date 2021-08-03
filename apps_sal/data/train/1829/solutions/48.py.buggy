# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, q):
            if node:
                res=0
                print (node.val,\" hello \",q)
                if node.val>= q:
                    res+=1
                res+=dfs(node.left,max(node.val,q))
                res+=dfs(node.right,max(node.val,q))
                return res
            else: return 0

        
        return dfs(root,-10001)
        
