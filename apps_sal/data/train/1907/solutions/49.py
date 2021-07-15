# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def rootOrder(self, root, target):
        if not root:
            return 0
        print(root.val)
        if root.val == target.val:
            self.ans = root
        self.rootOrder(root.left, target)
        self.rootOrder(root.right, target)
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.rootOrder(cloned, target)
        return self.ans
