# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        q = [(root, float('-inf'))]

        while q:
            (curr, maxvals) = q.pop(0)
            if curr.val >= maxvals:
                ans += 1
                maxvals = curr.val

            if curr.left:
                q.append((curr.left, maxvals))
            if curr.right:
                q.append((curr.right, maxvals))

        return ans
