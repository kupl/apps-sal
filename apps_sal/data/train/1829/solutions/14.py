# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sumNode = []
        self.goodNode(root, -234627, sumNode)
        return len(sumNode)
    
    def goodNode(self, root, maxSoFar, sumNode):
        if root is None:
            return
        
        #print(\"MaxSoFar\", maxSoFar)
        #print(\"Root val\", root.val)
        print((root.val))
        
        if root.val >= maxSoFar:
            #print(\"Added\", root.val)
            sumNode.append(root.val)
            #print(sumNode)
        
        maxSoFarNow = max(maxSoFar, root.val)
        
        self.goodNode(root.left, maxSoFarNow, sumNode)
        self.goodNode(root.right, maxSoFarNow, sumNode)
        
        
        
        
        

        

