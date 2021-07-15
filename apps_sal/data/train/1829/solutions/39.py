# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def order(root, maxi):
    if root is None:
        return 0
    
    count = 0
    if root.val >= maxi:
        count += 1
        maxi = root.val
        
    return count + order(root.left, maxi) + order(root.right, maxi)
    

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return order(root, root.val)
