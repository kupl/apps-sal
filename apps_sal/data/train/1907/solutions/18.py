# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [original]
        cloned_q = [cloned]
        while True:
            curr = queue.pop(0)
            cloned_curr = cloned_q.pop(0)
            if curr == target:
                return cloned_curr
            if curr.left:
                queue.append(curr.left)
                cloned_q.append(cloned_curr.left)
            if curr.right:
                queue.append(curr.right)
                cloned_q.append(cloned_curr.right)
