# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = []
        def DFS(node):
            if not node:
                return False
            if node is target:
                return True
            if DFS(node.left):
                path.append(\"Left\")
                return True
            if DFS(node.right):
                path.append('Right')
                return True
            return False
        DFS(original)
        cHead = cloned
        for node in reversed(path):
            if node == \"Left\":
                cHead = cHead.left
            else:
                cHead = cHead.right
        return cHead
                
