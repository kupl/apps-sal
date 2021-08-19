# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nxt = [cloned]
        while True:
            curr = nxt.pop()
            if curr.val == target.val:
                return curr
            else:
                if curr.left:
                    nxt.append(curr.left)
                if curr.right:
                    nxt.append(curr.right)
