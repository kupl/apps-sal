# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, rootA: TreeNode, rootB: TreeNode, inputA: TreeNode) -> TreeNode:
        q = deque([(rootA, rootB)])
        while q:
            nodeA, nodeB = q.popleft()
            if nodeA is inputA:
                return nodeB
            if nodeA.left is not None:
                q.append((nodeA.left, nodeB.left))
            if nodeA.right is not None:
                q.append((nodeA.right, nodeB.right))
        return None
    

