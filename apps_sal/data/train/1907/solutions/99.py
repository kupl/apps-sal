# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([cloned])
        while q:
            p = q.popleft()
            if p.val == target.val: return p
            q += [c for c in [p.left, p.right] if c]

