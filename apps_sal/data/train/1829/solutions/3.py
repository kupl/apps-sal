# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #preorder traverse, keeping track of the max for that path
        #if X is >= the max on the path, numGoodNodes += 1
        
        stack = [(root, root.val)]
        count = 0
        
        while stack:
            cur, greatest = stack.pop()
            if cur:
                if cur.val >= greatest:
                    count += 1

                if cur.right:
                    stack.append((cur.right, max(cur.right.val, greatest)))
                if cur.left:
                    stack.append((cur.left, max(cur.left.val, greatest)))
                       
        return count

                       

                       


        
        

