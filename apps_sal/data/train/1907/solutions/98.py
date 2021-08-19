# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        currNodes = [original]
        corrNodes = [cloned]
        while(len(currNodes)):
            currNode = currNodes.pop()
            corrNode = corrNodes.pop()
            if currNode is not None:
                if currNode is target:
                    return corrNode
                if currNode.left is not None:
                    currNodes.insert(0, currNode.left)
                    corrNodes.insert(0, corrNode.left)
                if currNode.right is not None:
                    currNodes.insert(0, currNode.right)
                    corrNodes.insert(0, corrNode.right)
        return None
