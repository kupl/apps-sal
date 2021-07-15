# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        candidates = []
        def dfs(node):
            if not node:
                return 0
 
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                l and candidates.append(l)
                r and candidates.append(r)
            return 1 + l + r
        # candidates now contain left and right subtree of the   node with val x
        # Get the length of subtree of parent node
        dfs(root)
        # print(candidates)
        # if root.val != x:
        candidates.append(n - (1 + sum(candidates)))
        return any(mine > (n-mine) for mine in candidates)
        
  
                
                
                

