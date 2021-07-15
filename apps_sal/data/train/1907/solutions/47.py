# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        \"\"\"
        Focus on simple case of no repeated values, this means
        \"\"\"
        
        # assume node is in tree
        
        # find node in tree recursively
        
        def findNode(searchNode: TreeNode, target: TreeNode, current_directions = None) -> TreeNode:
            
            currentNode = searchNode
            if current_directions == None:
                current_directions = \"\"
            
            if currentNode == target:
                return current_directions
            elif currentNode == None:
                return None
            elif currentNode.left == None and currentNode.right == None:
                return None
            else:
                leftResult = findNode(currentNode.left, target, current_directions + \"L\")
                rightResult = findNode(currentNode.right, target, current_directions + \"R\")
                
                if leftResult:
                    return leftResult
                if rightResult:
                    return rightResult
            
            return None
        
        directions = findNode(original, target)
        print(directions)
        # traverse down tree from node
        nodeInNewTree = cloned

        for direction in directions:
            if direction == \"L\":
                nodeInNewTree = nodeInNewTree.left
            elif direction == \"R\":
                nodeInNewTree = nodeInNewTree.right

        return nodeInNewTree
            

\"\"\"        
        currentNode = cloned
        
        while currentNode != None:
            
            if target.val == currentNode.val:
                return currentNode
            elif target.val < currentNode.val: # go left
                currentNode = currentNode.left
            else: # go right
                currentNode = currentNode.right
\"\"\"
