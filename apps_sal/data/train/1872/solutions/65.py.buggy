# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ht(self, root):
        if (root == None):
            return 0
        return 1 + max(self.ht(root.left), self.ht(root.right))
    
    
    def Sum(self, root, SA, level):
        if (root != None):
            print (level)
            SA[level] += root.val
            if (root.left != None):
                self.Sum(root.left, SA, level + 1)
            if (root.right != None):
                self.Sum(root.right, SA, level + 1)
                
    def maxLevelSum(self, root: TreeNode) -> int:
        SA = [0]*self.ht(root)
        print(\"het \" + str(self.ht(root)))
        self.Sum(root, SA, 0)
        print (SA)
        return SA.index(max(SA)) + 1
            
            
        

